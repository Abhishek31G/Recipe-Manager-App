from django.contrib import admin
from .models import *
# Register your models here.

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register([Recipe, Department, StudentID, Student, Subject])
admin.site.register(SubjectMark, SubjectMarkAdmin)