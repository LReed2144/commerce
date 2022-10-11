from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


#create listings model
class Category(models.Model):
    categoryName = models.CharField(max_length=50)

   #display category 
    def __str__(self):
        return self.categoryName


class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,  related_name="userBid")


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=640)
    imageUrl = models.CharField(max_length=1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    isActive = models.BooleanField(default=True)
    #will delete the user if admin deletes the user.  owner is a foreign key
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,  related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listingWatchlist")

    #display listing
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.author} comment on {self.listing}"

