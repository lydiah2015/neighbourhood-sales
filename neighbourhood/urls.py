"""neighbourhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from neighbourhood.views import IndexView, EditProfileView,ProfileView,\
                                NeighbourhoodProfileView,PostsView,CreateProductsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # neighbourhood urls
    url(r"^$",IndexView.as_view(),name="neighbourhood.index"),
    url(r"^profile$",ProfileView.as_view(),name="neighbourhood.profile"),

    url(r"^neighbourhood$",NeighbourhoodProfileView.as_view(),name="neighbourhood.neighbourhood"),
    url(r"^edit_profile$",EditProfileView.as_view(),name="neighbourhood.edit-profile"),
    url(r"^create_edit_posts$",PostsView.as_view(),name="neighbourhood.create-edit-posts"),
    url(r"^create_edit_products$",CreateProductsView.as_view(),name="neighbourhood.create-edit-products"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)