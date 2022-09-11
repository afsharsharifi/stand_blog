from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='post_list'),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('search', views.search_posts, name='search_posts'),
    path('archive', views.ArchiveIndexArticleView.as_view(), name='archive_view'),
    path('like/<slug:slug>/<int:pk>', views.like_view, name='like_view'),
    path('<slug:slug>', views.ArticleDetail.as_view(), name='post_detail'),
]
