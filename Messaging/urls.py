from  django.urls import path

from .views import *

urlpatterns = [

    path('addMessagetoDialog/<int:dialogid>',CreateMessageView.as_view()),
    path('updatemessageseen/<int:pk>',SeenMessageUpdateView.as_view()),
    path('getOneDialog/<int:pk>',GetDialogView.as_view()),
    path('getOneMessage/<int:Pk>',GetMessageView.as_view()),
    path('getOneUserDialog/<int:owner>',GetOneUserDialogsView.as_view()),
    path('getOneDialogMessages/<int:dialog>',GetDialogMessagesView.as_view()),
    path('createDialog', CreateDialogView.as_view()),
    path('getAllDialogs',GetAllDialogsView.as_view()),
]