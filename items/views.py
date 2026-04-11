from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LostItem, FoundItem, DEPARTMENT_CHOICES
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LostItemForm, FoundItemForm, FoundItemCreateForm
from django.shortcuts import get_object_or_404

def homepage(request):
    leaderboard = (
        FoundItem.objects.exclude(found_by__isnull=True)
        .exclude(found_by__exact='')
        .values('found_by', 'department')
        .annotate(number_of_items_found=Count('id'))
        .order_by('-number_of_items_found', 'found_by')[:10]
    )
    return render(request, 'lostandfound/home.html', {'leaderboard': leaderboard})

def lostitems(request):
    query = request.GET.get('q', '').strip()
    items = LostItem.objects.all().order_by('-date_lost')
    if query:
        items = items.filter(name__icontains=query)

    context = {
        'items': items,
        'query': query,
    }

    return render(request, 'lostandfound/lostitems.html', context)


def founditems(request):
    query = request.GET.get('q', '').strip()
    items = FoundItem.objects.all().order_by('-date_claimed')
    if query:
        items = items.filter(name__icontains=query)

    context = {
        'items': items,
        'query': query,
    }

    return render(request, 'lostandfound/founditems.html', context)

def manager_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name='Manager').exists():
            login(request, user)
            return redirect('/manager/dashboard/')

        else:
            return render(request, 'manager/login.html', {'error': 'Invalid credentials'})

    return render(request, 'manager/login.html')

def manager_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('homepage')


@login_required
def manager_dashboard(request):

    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    context = {
        'lost_items': lost_items,
        'found_items': found_items
    }

    return render(request, 'manager/dashboard.html', context)


@login_required
def add_lost_item(request):

    if request.method == "POST":

        form = LostItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Lost item added successfully.")
        else:
            messages.error(request, "Could not add lost item. Please check the form.")

    return redirect('manage_lost_items')

@login_required
def edit_lost_item(request, id):

    item = get_object_or_404(LostItem, id=id)

    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Lost item updated successfully.")
        else:
            messages.error(request, "Could not update lost item. Please check the form.")

    return redirect('manage_lost_items')

@login_required
def delete_lost_item(request, id):

    item = get_object_or_404(LostItem, id=id)
    item.delete()
    messages.success(request, "Lost item deleted successfully.")

    return redirect('manage_lost_items')

@login_required
def add_found_item(request):

    if request.method == "POST":
        form = FoundItemCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Found item added successfully.")
        else:
            messages.error(request, "Could not add found item. Please check the form.")

    return redirect('manage_found_items')

@login_required
def edit_found_item(request, id):

    item = get_object_or_404(FoundItem, id=id)

    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Found item updated successfully.")
        else:
            messages.error(request, "Could not update found item. Please check the form.")

    return redirect('manage_found_items')

@login_required
def delete_found_item(request, id):

    item = get_object_or_404(FoundItem, id=id)
    item.delete()
    messages.success(request, "Found item deleted successfully.")

    return redirect('manage_found_items')

@login_required
def manage_lost_items(request):
    query = request.GET.get('q', '').strip()
    items = LostItem.objects.all()
    if query:
        items = items.filter(name__icontains=query)
    items = items.order_by('-date_lost')
    form = LostItemForm()

    return render(request, 'manager/manage_lost_items.html', {
        'items': items,
        'form': form,
        'department_choices': DEPARTMENT_CHOICES,
        'query': query,
    })


@login_required
def manage_found_items(request):
    query = request.GET.get('q', '').strip()
    items = FoundItem.objects.all()
    if query:
        items = items.filter(name__icontains=query)
    items = items.order_by('-date_claimed')
    form = FoundItemCreateForm()

    return render(request, 'manager/manage_found_items.html', {
        'items': items,
        'form': form,
        'department_choices': DEPARTMENT_CHOICES,
        'query': query,
    })

@login_required
def mark_as_found(request, id):

    item = LostItem.objects.get(id=id)

    if request.method == "POST":

        found_by = request.POST.get('found_by')
        found_by_email = request.POST.get('found_by_email')
        department = request.POST.get('department')
        found_in = request.POST.get('found_in')
        date_found = request.POST.get('date_found')

        FoundItem.objects.create(
            name=item.name,
            description=item.description,
            found_in=found_in,
            found_by=found_by,
            found_by_email=found_by_email or None,
            department=department,
            date_found=date_found,
            image=item.image
        )

        item.delete()

    return redirect('manage_lost_items')


@login_required
def statistics(request):
    if not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You are not allowed to access statistics.")
        return redirect('homepage')

    current_lost_items_count = LostItem.objects.count()
    total_found_items_count = FoundItem.objects.count()
    claimed_items_count = FoundItem.objects.filter(status='Claimed').count()
    unclaimed_items_count = FoundItem.objects.filter(status='Unclaimed').count()
    overall_lost_items_count = current_lost_items_count + total_found_items_count

    lost_by_department = {}
    for department, _ in DEPARTMENT_CHOICES:
        current_count = LostItem.objects.filter(department=department).count()
        found_count = FoundItem.objects.filter(department=department).count()
        lost_by_department[department] = current_count + found_count

    leaderboard = (
        FoundItem.objects.exclude(found_by__isnull=True)
        .exclude(found_by__exact='')
        .values('found_by', 'department')
        .annotate(number_of_items_found=Count('id'))
        .order_by('-number_of_items_found', 'found_by')
    )

    context = {
        'overall_lost_items_count': overall_lost_items_count,
        'current_lost_items_count': current_lost_items_count,
        'claimed_items_count': claimed_items_count,
        'unclaimed_items_count': unclaimed_items_count,
        'lost_by_department_labels': list(lost_by_department.keys()),
        'lost_by_department_data': list(lost_by_department.values()),
        'leaderboard': leaderboard,
    }

    return render(request, 'manager/statistics.html', context)

