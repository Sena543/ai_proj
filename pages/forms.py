from django import forms
from .models import ImageUpload

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ('patientID', 'image')
    #image = forms.ImageField(required=False)