# Generated by Django 5.0.6 on 2024-07-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
