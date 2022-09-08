from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='post_list'),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('search', views.search_posts, name='search_posts'),
    path('red', views.HomePageRedirect.as_view(), name='red_view'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
]
