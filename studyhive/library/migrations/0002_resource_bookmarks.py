# Generated by Django 5.0.6 on 2024-09-28 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarked_resources', through='library.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]