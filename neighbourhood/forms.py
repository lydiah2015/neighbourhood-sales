from django import forms
from neighbourhood.models import Profile,Neighbourhood,Post,Product

class ProfileForm(forms.ModelForm):
    '''
    user profile form
    '''
    class Meta:
        model=Profile
        fields=['first_name',
                'last_name',
                'neighbourhood',
                'biography',
                'profile_photo']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            "title",
            "body"
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            "name","description","category","price","stock","photo"
        ]