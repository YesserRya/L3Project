# Generated by Django 4.0.3 on 2022-04-27 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mymedia', '0006_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='created',
        ),
    ]
