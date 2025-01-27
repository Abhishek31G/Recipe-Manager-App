from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User = get_user_model()

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

def update_recipe(request, slug):
    queryset = Recipe.objects.get(slug=slug)

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

def get_student(request):
    students = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        students = Student.objects.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) |
            Q(student_address__icontains = search)
        )
    paginator = Paginator(students, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "students" : page_obj,
    }
    return render(request, 'report/students.html', context)


def see_marks(request, student_id):
    student = SubjectMark.objects.filter(student__student_id__student_id = student_id)
    student_name = Student.objects.get(student_id__student_id=student_id)
    total_marks = student.aggregate(total_marks = Sum('marks'))
    percentage = round((total_marks['total_marks']/1100) * 100, 2)
    cgpa = round(percentage/9.5, 2)
    context ={
        "student" : student,
        "total_marks" : total_marks,
        "student_name" : student_name,
        "percentage"   : percentage,
        "cgpa" : cgpa,
    }
    return render(request,'report/see_marks.html', context)
