# Generated by Django 4.0.2 on 2023-01-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_grouping_order_product_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.BooleanField(default=0),
        ),
    ]
