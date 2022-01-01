from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipesForm
from django.views.generic import DetailView


def recipes_home(request):
    recipes = Recipes.objects.order_by('-date')
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})


class RecipesDetailView(DetailView):
    model = Recipes
    template_name = 'recipes/details_view.html'
    context_object_name = 'recipe'


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
