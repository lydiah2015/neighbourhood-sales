from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from neighbourhood.forms import ProfileForm,PostForm,ProductForm
from neighbourhood.models import Profile,Neighbourhood,Post,Product
from neighbourhood.decorators import has_profile

class IndexView(View):
    http_method_names = ['get']
    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        products= request.user.profile.neighbourhood.products.all()
        return render(request,"core/index.html",{"products":products})

class ProfileView(View):
    http_method_names = ['get']
    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        products=request.user.profile.profile_products.all()
        # print("posts")
        # print(posts)
        return render(request,"core/profile.html",{"products":products})

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
        
class NeighbourhoodProfileView(View):
    http_method_names = ['get']
    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        businesses=request.user.profile.neighbourhood.businesses.all()
        contacts=request.user.profile.neighbourhood.contacts.all()
        return render(request,"core/neighbourhood.html",{"businesses":businesses,"contacts":contacts})


class PostsView(View):
    http_method_names = ['get','post']
    def create_post_form(self,request):
        post_id=request.GET.get("post_id",None)
        form=PostForm()
        if post_id:
            try:
                form=PostForm(instance=get_object_or_404(Post,pk=int(post_id)))
            except:
                pass
        return form

    def save_create_edit_post_form(self,request):
        print(request.GET)
        post_id=request.GET.get("post_id",None)
        form=PostForm(request.POST,request.FILES)
        print(post_id)
        if post_id != None:
            try:
                p=Post.objects.get(pk=int(post_id))
                form=PostForm(request.POST,request.FILES,instance=p)
            except Post.DoesNotExist:
                pass
        if form.is_valid():
            post=form.save(commit=False)
            post.profile=request.user.profile
            post.neighbourhood=request.user.profile.neighbourhood
            post.save()
            return True,form
        return False,form

    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        post_id=request.GET.get("post_id",None)
        form =self.create_post_form(request)
        return render(request,"core/create_edit_post.html",{"form":form,"post_id":post_id})

    @method_decorator([login_required,has_profile])
    def post(self,request,*args, **kwargs):
        status,form=self.save_create_edit_post_form(request)
        if status==True:
            return redirect("neighbourhood.index")
        return render(request,"core/create_edit_post.html",{"form":form})


class CreateProductsView(View):
    http_method_names = ['get','post']
    def create_product_form(self,request):
        product_id=request.GET.get("product_id",None)
        form=ProductForm()
        if product_id:
            try:
                form=ProductForm(instance=get_object_or_404(Product,pk=int(product_id)))
            except:
                pass
        return form

    def save_create_edit_product_form(self,request):
        print(request.GET)
        product_id=request.GET.get("product_id",None)
        form=ProductForm(request.POST,request.FILES)
        print(product_id)
        if product_id != None:
            try:
                p=Product.objects.get(pk=int(product_id))
                form=ProductForm(request.POST,request.FILES,instance=p)
            except Product.DoesNotExist:
                pass
        if form.is_valid():
            product=form.save(commit=False)
            product.seller=request.user.profile
            product.neighbourhood=request.user.profile.neighbourhood
            product.save()
            return True,form
        return False,form

    @method_decorator([login_required,has_profile])
    def get(self,request,*args, **kwargs):
        product_id=request.GET.get("product_id",None)
        form =self.create_product_form(request)
        return render(request,"core/create_edit_product.html",{"form":form,"product_id":product_id})

    @method_decorator([login_required,has_profile])
    def post(self,request,*args, **kwargs):
        status,form=self.save_create_edit_product_form(request)
        if status==True:
            return redirect("neighbourhood.index")
        return render(request,"core/create_edit_product.html",{"form":form})