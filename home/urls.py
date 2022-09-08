from django.urls import path

from . import views

urlpatterns = [
    path('sidebar-partial', views.sidebar_partial, name="sidebar_partial"),
    path('', views.index_page, name="index"),
    path('contact', views.ContactUsView.as_view(), name="contact"),
    path('send-message', views.MessageView.as_view(), name="send_message"),
    path('messages-list', views.MessageListView.as_view(), name="messages_list"),
    path('edit-message/<int:pk>', views.MessageUpdateView.as_view(), name="edit_message"),
    path('delete-message/<int:pk>', views.MessageDeleteView.as_view(), name="delete_message"),
]
