# Generated by Django 4.0.3 on 2022-05-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mymedia', '0014_post_img_delete_imagepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
