# Generated by Django 5.0.3 on 2024-03-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='salePrice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
