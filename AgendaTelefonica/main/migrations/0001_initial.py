# Generated by Django 5.1.1 on 2024-09-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('lastName', models.CharField(max_length=35)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('phoneNumberWork', models.CharField(max_length=10)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]