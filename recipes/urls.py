
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("new/", views.new_recipe, name="new_recipe"),
    path("profile/<str:username>/", views.ProfileView, name="profile"),
]
