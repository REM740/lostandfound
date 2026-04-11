from django import forms
from .models import LostItem, FoundItem, DEPARTMENT_CHOICES

INPUT_CLASS = 'w-full border border-gray-300 rounded px-3 py-2'


def _apply_input_styling(form):
    for field in form.fields.values():
        w = field.widget
        if isinstance(w, forms.ClearableFileInput):
            w.attrs['class'] = INPUT_CLASS
        elif isinstance(w, forms.Select):
            w.attrs['class'] = INPUT_CLASS
        elif isinstance(w, forms.Textarea):
            w.attrs['class'] = INPUT_CLASS
        elif isinstance(w, forms.DateInput):
            w.input_type = 'date'
            w.attrs['type'] = 'date'
            w.attrs['class'] = INPUT_CLASS
        else:
            w.attrs['class'] = INPUT_CLASS


class LostItemForm(forms.ModelForm):

    class Meta:
        model = LostItem
        fields = [
            'name',
            'description',
            'lost_in',
            'lost_by',
            'lost_by_email',
            'department',
            'date_lost',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget = forms.Select(
            choices=[('', '---------')] + DEPARTMENT_CHOICES,
            attrs={'class': INPUT_CLASS},
        )
        _apply_input_styling(self)


class FoundItemForm(forms.ModelForm):

    class Meta:
        model = FoundItem
        fields = [
            'name',
            'description',
            'found_in',
            'found_by',
            'found_by_email',
            'department',
            'date_found',
            'status',
            'claimed_by',
            'claimed_by_email',
            'date_claimed',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget = forms.Select(
            choices=[('', '---------')] + DEPARTMENT_CHOICES,
            attrs={'class': INPUT_CLASS},
        )
        _apply_input_styling(self)


class FoundItemCreateForm(forms.ModelForm):

    class Meta:
        model = FoundItem
        fields = [
            'name',
            'description',
            'found_in',
            'found_by',
            'found_by_email',
            'department',
            'date_found',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget = forms.Select(
            choices=[('', '---------')] + DEPARTMENT_CHOICES,
            attrs={'class': INPUT_CLASS},
        )
        _apply_input_styling(self)
