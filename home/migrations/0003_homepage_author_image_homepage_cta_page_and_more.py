# Generated by Django 5.1.1 on 2024-10-02 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='author_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='my_story_content',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='homepage',
            name='my_story_title',
            field=models.CharField(blank=True, default='My Story', max_length=40),
        ),
        migrations.AddField(
            model_name='homepage',
            name='summary',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]