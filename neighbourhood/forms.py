from django import forms
from neighbourhood.models import Profile,Neighbourhood

class ProfileForm(forms.ModelForm):
    '''
    user profile form
    '''
    # neighbourhood_choices=tuple((n.name,n.name) for n in Neighbourhood.objects.all())
    # neighbourhood=forms.ChoiceField(label="neighbourhood",choices=neighbourhood_choices)
    class Meta:
        model=Profile
        fields=['first_name',
                'last_name',
                'neighbourhood',
                'biography',
                'profile_photo']