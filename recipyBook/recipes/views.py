from django.shortcuts import render
from .models import Recipes


def recipes_home(request):
    recipes = Recipes.objects.order_by('-date')
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})
