# Generated by Django 5.0.6 on 2024-07-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=25)),
                ('subject', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
