# Generated by Django 2.2.4 on 2019-09-12 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190909_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='biografi',
            new_name='biography',
        ),
    ]