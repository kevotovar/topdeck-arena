# Generated by Django 2.1 on 2018-08-16 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='name',
        ),
    ]