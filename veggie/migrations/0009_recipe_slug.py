# Generated by Django 5.0.4 on 2024-07-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0008_alter_subjectmark_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]