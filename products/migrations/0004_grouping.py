# Generated by Django 4.0.2 on 2022-12-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]