
from recipes.models import ShoppingList
from django.urls import path
from django.urls.conf import include
from user import views as views_user
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
from api.views import GetIngredient


urlpatterns = [
    path('favorites/', views.AddToFavorites.as_view()),
    path('favorites/<int:id>/', views.RemoveFromFavorites.as_view()),
    path('purchases/<int:pk>/', views.remove_purchase, name='delete_purchase'),
    path('purchases/', views.PurchaseView.as_view()),
    path('ingredients/', GetIngredient.as_view({'get': 'list'}))
]
