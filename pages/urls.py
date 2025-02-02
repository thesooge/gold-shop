
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.profile, name="profile"),
    path("profile/update", views.edit_user_profile, name="update-profile"),

]