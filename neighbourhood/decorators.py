from django.shortcuts import render, redirect
from neighbourhood.models import Profile

def has_profile(function):
    def wrap(request, *args, **kwargs):
        try:
            if request.user.profile:
                return function(request, *args, **kwargs)
        except Profile.DoesNotExist:
            return redirect("neighbourhood.edit-profile")
    return wrap
