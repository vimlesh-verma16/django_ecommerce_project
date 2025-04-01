# Generated by Django 5.1.7 on 2025-04-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_timestamp'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='product',
        ),
        migrations.AddField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]
