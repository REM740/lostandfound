from django import forms
from .models import LostItem, FoundItem


class LostItemForm(forms.ModelForm):

    class Meta:
        model = LostItem
        fields = ['name', 'description', 'lost_in','lost_by', 'date_lost', 'image']

        widgets = {
            'date_lost': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'border rounded px-3 py-2 w-full'
                }
            )
        }


class FoundItemForm(forms.ModelForm):

    class Meta:
        model = FoundItem
        fields = ['name', 'description', 'found_in', 'found_by', 'date_found', 'status', 'claimed_by', 'date_claimed', 'image']

        widgets = {
            'date_found': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'border rounded px-3 py-2 w-full'
                }
            ),
            'date_claimed': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'border rounded px-3 py-2 w-full'
                }
            )
        }


class FoundItemCreateForm(forms.ModelForm):

    class Meta:
        model = FoundItem
        fields = ['name', 'description', 'found_in', 'found_by', 'date_found', 'image']

        widgets = {
            'date_found': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'border rounded px-3 py-2 w-full'
                }
            )
        }