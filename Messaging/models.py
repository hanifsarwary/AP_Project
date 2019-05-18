from django.db import models

# Create your models here.
from django.db import models

from django.conf import settings
from django.template.defaultfilters import date as dj_date
from django.utils.translation import ugettext as _
from django.utils.timezone import localtime



from django.db import models
from UserHandling.models import Profile
# Create your models here.


class Post(models.Model):
    post_text = models.CharField(max_length=1500)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)

    @property
    def user__username(self):
        return self.user.username

    def __str__(self):
        return self.post_text[:30]


class PostPicture(models.Model):
    picture = models.FileField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    @property
    def post__id(self):
        return self.post.id

    def __str__(self):
        return self.post.__str__()


class PostLike(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.post.__str__()+'.... is liked by '+self.profile.__str__()


class PostComment(models.Model):

    comment_text = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post.__str__()+'....  commented by '+self.author.__str__()

    class Meta:
        ordering = ["post_date"]
    #
    # def __str__(self):
    #
    #     len_title = 75
    #     if len(self.comment_text) > len_title:
    #         titlestring = self.comment_text[:len_title] + '...'
    #     else:
    #         titlestring = self.comment_text
    #     return titlestring


class Group(models.Model):
    group_admin = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    group_name = models.CharField(max_length=50,unique=True)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    picture = models.FileField(null=True,default=None)

    def __str__(self):
        return self.group_name+" is created by"+self.group_admin.__str__()


class GroupMembers(models.Model):
    member = models.ForeignKey(Profile,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.member.__str__()+self.group.__str__()


class GroupPost(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)+str(self.group)


class Dialog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Dialog owner"), related_name="selfDialogs",
                              on_delete=models.CASCADE)
    opponent = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Dialog opponent"), on_delete=models.CASCADE)

    def __str__(self):
        return _("Chat with ") + self.opponent.username


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, verbose_name=_("Dialog"), related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), related_name="messages",
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("Message text"))
    read = models.BooleanField(verbose_name=_("Read"), default=False)
    objects = models.Manager()
    message_time = models.TimeField(auto_now_add=True)
    message_date = models.DateField(auto_now_add=True)


    def get_formatted_create_datetime(self):
        return dj_date(localtime(self.created), settings.DATETIME_FORMAT)

    def __str__(self):
        return self.sender.username + "(" + self.get_formatted_create_datetime() + ") - '" + self.text + "'"