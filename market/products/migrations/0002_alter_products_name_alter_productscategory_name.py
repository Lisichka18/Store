# Generated by Django 4.2.2 on 2023-07-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='productscategory',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
