from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('search', views.search_posts, name='search_posts'),
    path('testbase', views.TestBaseView.as_view(), name='test_base'),
    path('testbase/amir', views.HelloToAmir.as_view(), name='test_base_amir'),
    path('testbase/ahmad', views.HelloToAhmad.as_view(), name='test_base_ahmad'),
    path('testbase/ali', views.HelloToAli.as_view(), name='test_base_ali'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
]
