# Generated by Django 4.2.9 on 2024-04-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]