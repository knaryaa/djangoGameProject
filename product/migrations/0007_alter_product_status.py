# Generated by Django 5.0.3 on 2024-03-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_saleprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
