from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
# Register your models here.

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register([Recipe, Department, StudentID, Student, Subject])
admin.site.register(SubjectMark, SubjectMarkAdmin)