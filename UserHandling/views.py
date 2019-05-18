from django.shortcuts import render
from .Serializer import *
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView,ListAPIView
from django.views import View
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status


class CreateProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TESTVIEW(View):

    def post(self,request):
        print(request.POST.get('email',False))
        return JsonResponse({"success":"success"})


class GetAllUserView(RetrieveAPIView):
    serializer_class = ProfileSendSerializer

    def get_queryset(self):
        return Profile.objects.all()


class GetUserCountView(View):

    def get(self,request):
        count = Profile.objects.all().count()
        data = {
             'count': count}

        return JsonResponse(data)


class GetSingleUser(RetrieveAPIView):

    serializer_class = ProfileSendSerializer

    def get_queryset(self):
        return Profile.objects.filter(pk=self.kwargs['pk'])


class GetUserByName(RetrieveAPIView):

    serializer_class = ProfileSendSerializer
    lookup_field = 'first_name'

    def get_queryset(self):
        return Profile.objects.filter(first_name__contains=self.kwargs['first_name'])


class GetUserByUsername(RetrieveAPIView):

    serializer_class = ProfileSendSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return Profile.objects.filter(username=self.kwargs['username'])


class GetUserFollowers(ListAPIView):
    serializer_class = GetFollowerFolloweeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return FollowerFollowing.objects.filter(followee=self.kwargs['pk'])


class CreateFollowerFollowee(CreateAPIView):
    serializer_class = FollowerFolloweeSerializer
    queryset = FollowerFollowing.objects.all()