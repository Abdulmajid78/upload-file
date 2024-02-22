from django import forms

from .models import ContactModel


class ContactsForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('full_name', 'group_name', 'radio', 'file')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                "id": "full_name"
            }),
            'group_name': forms.TextInput(attrs={
                "value": "FSP - ",
                'type': 'text',
                'class': 'form-control',
                "id": "group_name"
            }),
            'radio': forms.RadioSelect(attrs={
                'class': 'raddiioo text-white d-flex gap-3 mt-2',
                "id": "select"
            }),
            'file': forms.FileInput(attrs={  # Use FileInput widget for file field
                'class': 'form-control w-50',
                "id": "file"
            })
        }
