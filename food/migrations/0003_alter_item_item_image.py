# Generated by Django 5.0.6 on 2024-10-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_item_item_price_item_image_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://via.placeholder.com/150', max_length=500),
        ),
    ]
