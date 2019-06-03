from django.contrib import admin
from neighbourhood.models import Profile, Neighbourhood, Post, Location, Contact

admin.site.register(
    Neighbourhood,
    list_display=["name","created_at"],
    search_fields=["name"],
)

admin.site.register(
    Location,
    list_display=["name","created_at"],
    search_fields=["name"],
)

admin.site.register(
    Contact,
    list_display=["name","created_at"],
    search_fields=["name"],
)

admin.site.register(
    Profile,
    list_display=["user","created_at"],
    search_fields=["user__username"],
)