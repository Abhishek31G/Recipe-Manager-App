# Generated by Django 5.0.4 on 2024-07-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='recipe'),
        ),
    ]
