from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from neighbourhood.forms import ProfileForm
from neighbourhood.models import Profile,Neighbourhood
from neighbourhood.decorators import has_profile

class IndexView(View):
    http_method_names = ['get']
    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        return render(request,"core/index.html",{})


class ProfileView(View):
    http_method_names = ['get']
    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        return render(request,"core/profile.html",{})

class EditProfileView(View):
    @method_decorator(login_required)
    def get(self,request,*args, **kwargs):
        form=self.create_profile_form(request)
        return render(request,"core/create_profile.html",{"form":form})

    def create_profile_form(self,request):
        try:
            if request.user.profile:
                return ProfileForm(instance=request.user.profile)
        except Profile.DoesNotExist:
            return ProfileForm()


    def save_profile_form(self,request):
        try:
            if request.user.profile:
                form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        except Profile.DoesNotExist:
            form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return True,form
        return False,form
            
    @method_decorator(login_required)
    def post(self,request,*args, **kwargs):
        status,form=self.save_profile_form(request)
        if status==True:
            return redirect("neighbourhood.index")
        return render(request,"core/create_profile.html",{"form":form})
        

