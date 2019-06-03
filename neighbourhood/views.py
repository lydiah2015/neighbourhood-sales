from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(View):
    http_method_names = ['get','post']
    @method_decorator(login_required)
    def get(self,request,*args, **kwargs):
        return "True"