# Generated by Django 3.2.8 on 2022-01-20 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_product_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product categories'},
        ),
    ]
