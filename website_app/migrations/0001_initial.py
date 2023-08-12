# Generated by Django 4.2.1 on 2023-08-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('select_course', models.CharField(max_length=30)),
            ],
        ),
    ]