from django.utils.text import slugify
import uuid

def generate_slug(title:str)->str:
    from .models import Recipe
    title = slugify(title)

    """
    A Function to generate Slug for Receipe model which returns str
    """
    while(Recipe.objects.filter(slug=title).exists()):
         title = f"{slugify(title)}-{str(uuid.uuid4())[:6]}"
    return title