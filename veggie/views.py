from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login/")
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

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!')
            return redirect('/login/')
    
        user = authenticate(username=username, password=password)
    
        if user is None:
            messages.error(request, 'Invalid Password!')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        userName = User.objects.filter(username=username)
        userEmail = User.objects.filter(email=email)

        if userName.exists():
            messages.error(request, 'Username is already taken!')
            return redirect('/register/')
        if userEmail.exists():
            messages.error(request, 'Email already exists!')
            return redirect('/register/')

        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account successfully created!')
        return redirect('/register/')
    return render(request, 'register.html')
