from django.contrib import admin
from django.urls import path
from home.views import *
from veggie.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name="home"),
    path('base/', base, name="base"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('recipes/', recipes, name="recipes"),
    path('delete-recipe/<int:id>/', delete_recipe, name="delete_recipe"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: 
    urlpatterns += static (settings.MEDIA_URL, 
                           document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()
