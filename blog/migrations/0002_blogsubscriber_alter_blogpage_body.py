# Generated by Django 5.1.2 on 2024-10-29 09:23

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('content', 0), ('image', 1), ('quote', 2), ('video_block', 7), ('twitter_block', 9), ('code_block', 12), ('result_block', 13)], block_lookup={0: ('utils.models.UtilsCustomRichTextBlock', (), {}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {'template': 'blocks/image.html'}), 2: ('wagtail.blocks.BlockQuoteBlock', (), {'template': 'blocks/quote.html'}), 3: ('wagtail.blocks.CharBlock', (), {'required': False}), 4: ('wagtail.embeds.blocks.EmbedBlock', (), {'required': False}), 5: ('wagtail.documents.blocks.DocumentChooserBlock', (), {'required': False}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 7: ('wagtail.blocks.StructBlock', [[('title', 3), ('video_url', 4), ('video_file', 5), ('poster_image', 6)]], {'template': 'blocks/video_block.html'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.StructBlock', [[('text', 8)]], {'template': 'blocks/twitter_block.html'}), 10: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('python', 'Python'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('shell', 'Shell')], 'label': 'Language code'}), 11: ('wagtail.blocks.TextBlock', (), {'label': 'Source code'}), 12: ('wagtail.blocks.StructBlock', [[('language', 10), ('code', 11)]], {}), 13: ('utils.models.UtilsResultBlock', (), {})}),
        ),
    ]
