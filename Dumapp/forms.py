
from django import forms
from .models import ImageModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'quantity', 'description', 'delivery_address', 'contact_number']
        widgets = {
            'delivery_address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter full address'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the item(s)'}),
        }
