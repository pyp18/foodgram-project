from django.urls import path
from django.urls.conf import include
from user import views as views_user
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)


router.register(
    r'ingredients',
    views.GetIngredient,
    basename='ingredients'
)

urlpatterns = [
    path('favorites/', views.AddToFavorites.as_view()),
    path('favorites/<int:id>/', views.RemoveFromFavorites.as_view()),
    path('', include(router.urls)),
]
