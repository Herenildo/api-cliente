# Generated by Django 5.1.2 on 2024-10-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
