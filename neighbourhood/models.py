from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,
                related_name="profile",
                on_delete=models.CASCADE,null=True
    )
    neighbourhood=models.ForeignKey("neighbourhood.Neighbourhood",
                related_name="occupants",
                on_delete=models.CASCADE,null=True

    )
    first_name=models.CharField(max_length=255, null=True)
    last_name=models.CharField(max_length=255, null=True)
    biography=models.CharField(max_length=255, null=True)
    profile_photo = models.ImageField(upload_to = 'image/')
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "profile:{}".format(self.user.username)


class Location(models.Model):
    name=models.CharField(max_length=255, null=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Location:{}".format(self.name if self.name else self.id)


class Neighbourhood(models.Model):
    name=models.CharField(max_length=255, null=False, unique=True)
    location=models.ForeignKey("neighbourhood.Location",
                related_name="neighbourhoods",
                on_delete=models.CASCADE,null=True

    )
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name if self.name else self.id)

class Business(models.Model):
    name=models.CharField(max_length=255, null=True)
    neighbourhood=models.ForeignKey("neighbourhood.Neighbourhood",
                related_name="businesses",
                on_delete=models.CASCADE,null=True

    )
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "business:{}".format(self.name if self.name else self.id)

class Contact(models.Model):
    name=models.CharField(max_length=255, null=True)
    descripion=models.CharField(max_length=255, null=True)
    email=models.CharField(max_length=255, null=True)
    phone_number=models.CharField(max_length=255, null=True)
    neighbourhood=models.ForeignKey("neighbourhood.Neighbourhood",
                related_name="contacts",
                on_delete=models.CASCADE,null=True

    )
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "contact:{}".format(self.name if self.name else self.id)

class Post(models.Model):
    profile=models.ForeignKey("neighbourhood.Profile",
                related_name="profile_posts",
                on_delete=models.CASCADE,null=True
    )
    neighbourhood=models.ForeignKey("neighbourhood.Neighbourhood",
                related_name="posts",
                on_delete=models.CASCADE,null=True

    )
    body=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def body_as_list(self):
        return self.body.split("\n")

    def __str__(self):
        return "Post:{}".format(self.id)