from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from recipes.models import ShoppingList, Recipe
from recipes.models import Ingredient, Favorite
from .serializers import IngredientSerializer
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

class GetIngredient(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        ingredient = self.request.query_params.get('query')
        if ingredient is not None:
            queryset = queryset.filter(title__startswith=ingredient)
        return queryset


class AddToFavorites(APIView):

    def post(self, request, format=None):
        Favorite.objects.get_or_create(
            user=request.user,
            recipe_id=request.data["id"],
        )

        return Response({'success': True}, status=status.HTTP_200_OK)


class RemoveFromFavorites(APIView):

    def delete(self, request, id, format=None):
        recipe = Favorite.objects.filter(recipe_id=id, user=request.user)
        recipe.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class PurchaseView(APIView):

    def post(self, request):
        recipe_id = request.data.get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        ShoppingList.objects.get_or_create(user=request.user, recipe=recipe)
        return Response({'success': True})




def remove_purchase(request, pk):
    purchase = ShoppingList.objects.filter(user=request.user, recipe = pk)
    purchase.delete()
    return redirect('shopping_list')