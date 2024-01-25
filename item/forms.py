from django import forms
from .models import Item

INSERT_CLASSES = 'w-full py-4 ps-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'qty')

        widgets = {
            'category': forms.Select(attrs={
                'class': INSERT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INSERT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INSERT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INSERT_CLASSES
            }),
            'qty': forms.NumberInput(attrs={
                'class': INSERT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INSERT_CLASSES
            })
        }
