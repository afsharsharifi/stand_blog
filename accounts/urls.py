from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup_page, name="signup"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),
    path('edit-profile', views.edit_profile_page, name="edit_profile"),
]
