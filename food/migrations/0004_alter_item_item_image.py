# Generated by Django 5.0.6 on 2024-10-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://png.pngtree.com/png-vector/20190223/ourmid/pngtree-vector-picture-icon-png-image_695350.jpg', max_length=500),
        ),
    ]
