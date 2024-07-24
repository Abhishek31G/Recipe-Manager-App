from django.shortcuts import render, redirect
from home.utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

# Create your views here.


def send_email(request):
    subject = "This email is from Django server with Attachment" 
    message = "Hey please find this attach file with this email" 
    recipient_list = ["abhishekgandhewar@gmail.com"] 
    file_path = f"{settings.BASE_DIR}/main.xlsx" 
    send_email_with_attachment (subject, message, recipient_list,file_path)
    return redirect('/')

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