# Generated by Django 5.1.2 on 2024-10-29 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contactsubmission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsubmission',
            options={'verbose_name': 'Message de Contact', 'verbose_name_plural': 'Messages de Contact'},
        ),
    ]
