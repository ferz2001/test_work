from django import forms
from .models import Book, Profile


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'title', 'author', 'description', 'price']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['column_name', 'is_visible']
        widgets = {
            'is_visible': forms.CheckboxInput(),
        }