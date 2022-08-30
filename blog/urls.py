from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.post_detail, name='post_detail'),
]
