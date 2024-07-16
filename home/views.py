from django.shortcuts import render

# Create your views here.

def index(request):
    students = [
            {"name":"Abhi", "age": 24},
            {"name":"Akash", "age": 16},
            {"name":"Shree", "age": 31},
            {"name":"Ajay", "age": 18},
            {"name":"Pratik", "age": 28},
            ]
    context = {
        "students":students,
    }
    return render(request, 'home/index.html', context)

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')