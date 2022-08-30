from django.urls import path

from . import views

urlpatterns = [
    path('sidebar-partial', views.sidebar_partial, name="sidebar_partial"),
    path('', views.index_page, name="index"),
]
