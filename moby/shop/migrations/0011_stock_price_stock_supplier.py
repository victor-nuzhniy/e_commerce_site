# Generated by Django 4.0.4 on 2022-08-18 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.supplier', verbose_name='Поставщик'),
        ),
    ]
