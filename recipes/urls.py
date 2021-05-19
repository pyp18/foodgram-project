
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.signup, name='signup'),
    path("new/", views.new_recipe, name="new_recipe"),
    path("profile/<str:username>/", views.ProfileView.as_view(), name="profile"),
    path("recipes/<int:pk>/", views.RecipeDetailView.as_view(), name="recipe")
]
