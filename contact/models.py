from django.db import models

from wagtail.models import Orderable
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    FieldRowPanel,
)
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey


class ContactInformation(Orderable):
    """
    Represents a contact profile associated with a ContactPage.
    """

    page = ParentalKey(
        "ContactPage",
        related_name="contacts",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50, verbose_name="Full Name")
    email = models.EmailField(
        max_length=254, blank=True, verbose_name="Email Address"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="Phone Number",
        help_text="Enter a valid phone number (e.g., +33123456789).",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("phone_number"),
    ]

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"{self.name} ({self.email})"


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    template = "contact/contact_page.html"
    subpage_types = []
    parent_page_types = ["home.HomePage"]

    subtitle = models.CharField(max_length=255, blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("subtitle"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        InlinePanel("contacts", label="Contact Profiles"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ]
        ),
    ]

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"
