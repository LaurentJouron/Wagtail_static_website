# Generated by Django 5.1.1 on 2024-10-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpage_body'),
        ('project', '0002_alter_projectpage_body'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='UtilsCategory',
        ),
    ]