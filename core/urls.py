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
    path('login/', log_in, name="login"),
    path('logout/', log_out, name="logout"),
    path('register/', register, name="register"),
    path('recipes/', recipes, name="recipes"),
    path('delete-recipe/<int:id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<slug>/', update_recipe, name="update_recipe"),
    path('students/', get_student, name="get_student"),
    path('see_marks/<student_id>', see_marks, name="see_marks"),
    path('send_email/', send_email, name="send_email"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG: 
    urlpatterns += static (settings.MEDIA_URL, 
                           document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()
