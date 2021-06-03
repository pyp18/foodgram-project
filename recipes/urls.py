from django.urls import path
from django.urls.conf import include
from recipes import views
from user import views as views_user
from rest_framework.urlpatterns import format_suffix_patterns


views_patterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views_user.signup, name='signup'),
    path('new/', views.new_recipe, name='new_recipe'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe'),
    path('my_favorites/', views.FavouriteView.as_view(), name='my_favorites'),
    path('follow/<str:username>/', views.profile_follow, name='follow'),
    path('unfollow/<str:username>/', views.profile_unfollow, name='unfollow'),
    path('follow_recipe_page/<int:pk>/<str:username>/',
         views.profile_follow_recipe_page, name='follow_recipe_page'),
    path('unfollow_recipe_page/<int:pk>/<str:username>/',
         views.profile_unfollow_recipe_page, name='unfollow_recipe_page'),
    path('my_subscriptions/', views.my_subscriptions,
         name='my_subscriptions'),
    path('recipes/edit/<int:id>/', views.recipe_edit, name='edit'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('download_shoplist/', views.shopping_list_download,
         name='download_shoplist'),
    path('recipes/delete/<int:id>/', views.recipe_delete, name='recipe_delete'),
]

api_patterns = [

]

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('', include(views_patterns)),
    path('', include(format_suffix_patterns(api_patterns))),
]
