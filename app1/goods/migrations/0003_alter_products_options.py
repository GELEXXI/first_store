# Generated by Django 4.2 on 2024-02-01 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукти'},
        ),
    ]
