# Generated by Django 4.2.9 on 2024-04-23 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comingSoon', '0002_alter_newsuser_options_remove_newsuser_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsUser',
            new_name='MailList',
        ),
    ]