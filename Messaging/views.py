from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
# Create your views here.
from .serializer import *

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveAPIView,DestroyAPIView
# Create your views here.
from .models import *


class GetPostView(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostLikeCreateView(ListCreateAPIView):
    serializer_class = PostLikeSerializer

    def get_queryset(self):
        return PostLike.objects.filter(post__pk=self.kwargs['pk'])


class PostCommentCreateView(ListCreateAPIView):
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        return PostComment.objects.filter(post=self.kwargs['pk'])


class PostPictureCreateView(ListCreateAPIView):
    serializer_class = PostPictureSerializer

    def get_queryset(self):
        return PostPicture.objects.all()


class GroupCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()


class GroupMemberCreateView(ListCreateAPIView):
    serializer_class = GroupMemberSerializer

    def get_queryset(self):
        return GroupMembers.objects.filter(group=self.kwargs['pk'])


class GroupPostCreateView(ListCreateAPIView):
    serializer_class = GroupPostSerializer

    def get_queryset(self):
        return GroupPost.objects.filter(group=self.kwargs['pk'])


class GetGroupByIdView(RetrieveAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.filter(pk=self.kwargs['pk'])


class GetGroupByNameView(RetrieveAPIView):
    serializer_class = GroupSerializer
    lookup_field = 'group_name'

    def get_queryset(self):
        return Group.objects.filter(group_name=self.kwargs['group_name'])


class GetUserPost(RetrieveAPIView):
    serializer_class = PostSerializer
    lookup_field = 'user__username'

    def get_queryset(self):
        return Post.objects.filter(user__username=self.kwargs['user__username'])


class GetUserPostById(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user__pk=self.kwargs['pk'])


class PostDeleteView(DestroyAPIView):
    serializer_class = PostSerializer
    lookup_field = 'pk'


class LikeDeleteView(DestroyAPIView):
    serializer_class = PostLikeSerializer
    lookup_field = 'pk'


class CommentDeleteView(DestroyAPIView):
    serializer_class = PostCommentSerializer
    lookup_field = 'pk'


class CreateDialogView(CreateAPIView):
    serializer_class = DialogSerializer
    queryset = Dialog.objects.all()


class CreateMessageView(CreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(dialog=self.kwargs['dialogid'])


class SeenMessageUpdateView(UpdateAPIView):
    serializer_class = MessageSeenSerializer
    queryset = Message.objects.all()
    lookup_field = 'pk'


class GetDialogView(RetrieveAPIView):
    serializer_class = GETDialogSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Dialog.objects.filter(pk=self.kwargs['pk'])


class GetMessageView(RetrieveAPIView):
    serializer_class = GETMessageSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Message.objects.filter(pk=self.kwargs['pk'])


class GetAllDialogsView(ListAPIView):
    serializer_class = GETDialogSerializer
    queryset = Dialog.objects.all()


class GetOneUserDialogsView(ListAPIView):
    serializer_class = GETDialogSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        return Dialog.objects.filter(owner=self.kwargs['owner'])


class GetDialogMessagesView(RetrieveAPIView):
    serializer_class = GETMessageSerializer
    lookup_field = 'dialog'

    def get_queryset(self):
        return Message.objects.filter(dialog=self.kwargs['dialog'])


from django.shortcuts import render

# Create your views here.
