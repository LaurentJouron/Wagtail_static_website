# Generated by Django 5.1.2 on 2024-11-06 10:43

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_alter_miscpage_body'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiscPageCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.utilscategory')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='misc.miscpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]