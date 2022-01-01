from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipesForm


def recipes_home(request):
    recipes = Recipes.objects.order_by('-date')
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})


def create(request):
    error = ''
    if request.method == 'POST':
        form = RecipesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_home')
        else:
            error = 'Форма заполнена неверно'

    form = RecipesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'recipes/create.html', data)
