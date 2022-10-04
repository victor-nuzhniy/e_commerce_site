# Generated by Django 4.0.4 on 2022-07-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_complete_alter_order_date_ordered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='city',
            field=models.CharField(blank=True, max_length=80, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='sale',
            name='department',
            field=models.CharField(blank=True, max_length=6, verbose_name='Номер отделения'),
        ),
        migrations.AddField(
            model_name='sale',
            name='region',
            field=models.CharField(blank=True, max_length=80, verbose_name='Регион'),
        ),
    ]