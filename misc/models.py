from django.db import models
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel
from utils.models import (
    UtilsCodeBlock,
    UtilsResultBlock,
    UtilsCustomRichTextBlock,
    UtilsVideoBlock,
)


class Skill(Orderable):
    page = ParentalKey(
        "MiscPage", related_name="skill", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    panels = [
        FieldPanel("name"),
        FieldPanel("level"),
    ]


class MiscPage(Page):

    html_subtitle = models.TextField(
        max_length=2000,
        blank=True,
        help_text="This can include Raw HTML. Be careful!",
    )

    body = StreamField(
        [
            (
                "content",
                UtilsCustomRichTextBlock(),
            ),
            (
                "image",
                ImageChooserBlock(
                    template="blocks/image.html",
                ),
            ),
            (
                "video_block",
                UtilsVideoBlock(
                    template="blocks/video_block.html",
                ),
            ),
            (
                "quote",
                blocks.BlockQuoteBlock(
                    template="blocks/quote.html",
                ),
            ),
            (
                "twitter_block",
                blocks.StructBlock(
                    [
                        ("text", blocks.CharBlock()),
                    ],
                    template="blocks/twitter_block.html",
                ),
            ),
            (
                "code_block",
                UtilsCodeBlock(),
            ),
            (
                "result_block",
                UtilsResultBlock(),
            ),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("html_subtitle"),
        FieldPanel("body"),
        InlinePanel("skill", label="Skills"),
    ]
