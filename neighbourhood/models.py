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
    description=models.CharField(max_length=255, null=True)
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
    
    @classmethod
    def create_neighbourhood(cls,name):
        n=Neighbourhood(name=name)
        n.save()
        return n
    
    def delete_neigborhood(self):
        Neighbourhood.object.get(pk=self.pk).delete()

    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        try:
            return Neighbourhood.objects.get(id=neigborhood_id)
        except Neighbourhood.DoesNotExist:
            return None

    def update_neighborhood(self,name,location):
        self.name=name
        self.location=location
        self.save()
    
    def update_occupants(self,occ):
        self.occupants.add(occ)
        self.save()

class Business(models.Model):
    name=models.CharField(max_length=255, null=False)
    description=models.CharField(max_length=255, null=True)
    neighbourhood=models.ForeignKey("neighbourhood.Neighbourhood",
                related_name="businesses",
                on_delete=models.CASCADE,null=True

    )
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_business(cls):
        pass

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        return Business.objects.get(pk=business_id)

    def update_business(self,name,description):
        self.name=name
        self.description=description
        self.save()

    def __str__(self):
        return "business:{}".format(self.name if self.name else self.id)



class Contact(models.Model):
    name=models.CharField(max_length=255, null=False)
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
    title=models.CharField(max_length=255, null=True)
    body=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    inserted_at = models.DateTimeField(auto_now=True)

    def body_as_list(self):
        return self.body.split("\n")

    def __str__(self):
        return "Post:{}".format(self.id)
    
