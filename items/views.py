from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LostItem, FoundItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm, FoundItemForm, FoundItemCreateForm
from django.shortcuts import get_object_or_404

@login_required
def manager_logout(request):
    logout(request)
    return redirect('/lostandfound/')

def homepage(request):
    return render(request, 'lostandfound/home.html')

def lostitems(request):
    items = LostItem.objects.all().order_by('-date_lost')

    context = {
        'items': items
    }

    return render(request, 'lostandfound/lostitems.html', context)


def founditems(request):
    items = FoundItem.objects.all().order_by('-date_claimed')

    context = {
        'items': items
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

@login_required
def manager_logout(request):
    logout(request)
    return redirect('/lostandfound/')

@login_required
def manager_dashboard(request):

    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    context = {
        'lost_items': lost_items,
        'found_items': found_items
    }

    return render(request, 'manager/dashboard.html', context)

from django.shortcuts import redirect

@login_required
def add_lost_item(request):

    if request.method == "POST":

        form = LostItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    return redirect('manage_lost_items')

@login_required
def edit_lost_item(request, id):

    item = get_object_or_404(LostItem, id=id)

    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('manage_lost_items')

@login_required
def delete_lost_item(request, id):

    item = get_object_or_404(LostItem, id=id)
    item.delete()

    return redirect('/manager/dashboard/')

@login_required
def add_found_item(request):

    if request.method == "POST":
        form = FoundItemCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('manage_found_items')

    return redirect('manage_found_items')

@login_required
def edit_found_item(request, id):

    item = get_object_or_404(FoundItem, id=id)

    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('/manager/dashboard/')

    else:
        form = FoundItemForm(instance=item)

    return render(request, 'manager/edit_found_item.html', {'form': form})

@login_required
def delete_found_item(request, id):

    item = get_object_or_404(FoundItem, id=id)
    item.delete()

    return redirect('/manager/dashboard/')

@login_required
def manage_lost_items(request):

    items = LostItem.objects.all()
    form = LostItemForm()

    return render(request, 'manager/manage_lost_items.html', {
        'items': items,
        'form': form
    })


@login_required
def manage_found_items(request):

    items = FoundItem.objects.all()
    form = FoundItemCreateForm()

    return render(request, 'manager/manage_found_items.html', {
        'items': items,
        'form': form
    })

@login_required
def mark_as_found(request, id):

    item = LostItem.objects.get(id=id)

    if request.method == "POST":

        found_by = request.POST.get('found_by')
        found_in = request.POST.get('found_in')
        date_found = request.POST.get('date_found')

        FoundItem.objects.create(
            name=item.name,
            description=item.description,
            found_in=found_in,
            found_by=found_by,
            date_found=date_found,
            image=item.image
        )

        item.delete()

    return redirect('manage_lost_items')

