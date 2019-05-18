from django.urls import path,include
from .views import *
from rest_auth.views import LoginView,LogoutView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('createprofile',csrf_exempt(CreateProfileView.as_view())),
    path('apicreateprofile',(CreateProfileView.as_view())),
    #path('createprofile', csrf_exempt(TESTVIEW.as_view())),
    path('login',csrf_exempt(LoginView.as_view())),
    path('logout',LogoutView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('getuserbyname/<str:first_name>', GetUserByName.as_view()),
    path('getuserbyusername/<str:username>', GetUserByUsername.as_view()),
    path('getuserfollowers/<int:pk>', GetUserFollowers.as_view()),
    path('createfollower', CreateFollowerFollowee.as_view()),
    path('getuserbyid/<int:pk>', GetSingleUser.as_view()),
]