# Generated by Django 5.0.4 on 2024-07-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0004_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
