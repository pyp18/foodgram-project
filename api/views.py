from rest_framework import status, mixins, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from recipes.models import ShoppingList, Recipe
from recipes.models import Ingredient, Favorite
from .serializers import IngredientSerializer
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .permissions import IsLogged, IsOwner


class GetIngredient(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsLogged,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class AddToFavorites(APIView):
    permission_classes = (IsLogged,)

    def post(self, request, format=None):
        Favorite.objects.get_or_create(
            user=request.user,
            recipe_id=request.data.get('id'),
        )

        return Response({'success': True}, status=status.HTTP_200_OK)


class RemoveFromFavorites(APIView):
    permission_classes = (IsLogged, IsOwner)

    def delete(self, request, id, format=None):
        recipe = get_object_or_404(Favorite, recipe_id=id, user=request.user)
        recipe.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)


class PurchaseView(APIView):
    permission_classes = (IsLogged,)

    def post(self, request):
        recipe_id = request.data.get('id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        ShoppingList.objects.get_or_create(user=request.user, recipe=recipe)
        return Response({'success': True})


@login_required
def remove_purchase(request, pk):
    purchase = get_object_or_404(ShoppingList, user=request.user, recipe=pk)
    purchase.delete()
    return redirect('shopping_list')
