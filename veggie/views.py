from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.

def recipes(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        return redirect('/recipes/')
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        search_term = request.GET.get('search')
        # queryset = queryset.filter(recipe_name__icontains = search_term)
        queryset = queryset.filter(Q(recipe_name__icontains=search_term) | Q(recipe_description__icontains=search_term))
    context = {
        "recipes": queryset,
    }
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/recipes/')
    context = {
        "recipe": queryset
    }
    return render(request, 'update_recipe.html', context)
