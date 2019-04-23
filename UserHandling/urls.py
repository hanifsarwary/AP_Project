from django.urls import path,include
from .views import *
urlpatterns = [
    path('createprofile',CreateProfileView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('getuserbyname/<str:first_name>', GetUserByName.as_view()),
    path('getuserbyusername/<str:username>', GetUserByUsername.as_view()),
    path('getuserfollowers/<int:pk>', GetUserFollowers.as_view()),
    path('createfollower', CreateFollowerFollowee.as_view()),
    path('getuserbyid/<int:pk>', GetSingleUser.as_view()),
]