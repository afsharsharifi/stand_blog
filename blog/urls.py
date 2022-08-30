from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
]
