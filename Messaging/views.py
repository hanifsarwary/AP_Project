from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
# Create your views here.
from .serializer import *


class CreateDialogView(CreateAPIView):
    serializer_class = DialogSerializer
    queryset = Dialog.objects.all()


class CreateMessageView(CreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(dialog=self.kwargs['dialogid'])


class SeenMessageUpdateView(UpdateAPIView):
    serializer_class = MessageSeenSerializer
    lookup_field = 'pk'


class GetDialogView(RetrieveAPIView):
    serializer_class = DialogSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Dialog.objects.get(pk=self.kwargs['pk'])


class GetMessageView(RetrieveAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Message.all_objects.get(pk=self.kwargs['pk'])


class GetAllDialogsView(ListAPIView):
    serializer_class = DialogSerializer
    queryset = Dialog.objects.all()


class GetOneUserDialogsView(ListAPIView):
    serializer_class = DialogSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        return Dialog.objects.filter(owner=self.kwargs['owner'])


class GetDialogMessagesView(RetrieveAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'dialog'

    def get_queryset(self):
        return Message.all_objects.filter(dialog=self.kwargs['dialog'])


from django.shortcuts import render

# Create your views here.
