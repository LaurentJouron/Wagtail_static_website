from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ValidationError

from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock
from datetime import datetime

from utils.models import (
    UtilsCodeBlock,
    UtilsResultBlock,
    UtilsCustomRichTextBlock,
    UtilsVideoBlock,
)


def validate_year(value):
    """Validates that the year is a positive integer within a reasonable range."""
    current_year = datetime.now().year
    if value < 1980 or value > current_year:
        raise ValidationError(
            f"L'année doit être comprise entre 1980 et {current_year}."
        )


class ExperienceIndexPage(Page):
    max_count = 1
    subpage_types = ["experience.ExperiencePage"]
    parent_page_types = ["home.HomePage"]

    summary = models.TextField(blank=True, max_length=500)

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
    ]

    def get_context(self, request):
        """Custom context to include paginated list of experiences."""
        context = super().get_context(request)
        experiences = (
            ExperiencePage.objects.live()
            .public()
            .order_by("-first_published_at")
        )
        paginator = Paginator(experiences, 5)
        page = request.GET.get("page", 1)

        try:
            experiences = paginator.page(page)
        except PageNotAnInteger:
            experiences = paginator.page(1)
        except EmptyPage:
            experiences = paginator.page(paginator.num_pages)

        context["experiences"] = experiences
        return context


class ExperiencePage(Page):
    parent_page_types = ["experience.ExperienceIndexPage"]
    logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        help_text="Company logo",
    )
    date_in = models.IntegerField(
        "Date d'entrée",
        validators=[validate_year],
        blank=True,
        null=True,
        help_text="Année de début de l'expérience",
    )
    date_out = models.IntegerField(
        "Date de sortie",
        validators=[validate_year],
        blank=True,
        null=True,
        help_text="Année de fin de l'expérience (laisser vide si actuelle)",
    )
    summary = models.TextField(
        max_length=500,
        help_text="Résumé de l'expérience",
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
                "quote",
                blocks.BlockQuoteBlock(
                    template="blocks/quote.html",
                ),
            ),
            (
                "video_block",
                UtilsVideoBlock(
                    template="blocks/video_block.html",
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
        FieldPanel("summary"),
        FieldPanel("logo"),
        FieldPanel("date_in"),
        FieldPanel("date_out"),
        FieldPanel("body"),
    ]

    def clean(self):
        """Custom validation to ensure date_out is not before date_in."""
        if self.date_out and self.date_out < self.date_in:
            raise ValidationError(
                "La date de fin ne peut pas être antérieure à la date de début."
            )
        super().clean()

    def __str__(self):
        return f"{self.title} ({self.date_in} - {self.date_out or 'présent'})"
