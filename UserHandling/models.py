from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    profile_pic = models.FileField(upload_to='profile pictures',null=True,blank=True)
    average_rating = models.FloatField(default=0,blank=True,null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.",null=True,blank=True)

    def __str__(self):
        return self.first_name+' '+self.last_name


class FollowerFollowing(models.Model):
    followee = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='followee')
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='follower'
                                 )

    def __str__(self):
        return self.followee.__str__()+' is followed by '+self.follower.__str__()

    class Meta:
        unique_together = ('follower','followee')

