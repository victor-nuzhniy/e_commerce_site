# Generated by Django 4.0.4 on 2022-06-20 08:38

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.user_directory_path_2),
        ),
    ]