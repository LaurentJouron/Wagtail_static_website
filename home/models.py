from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from blog.models import BlogIndexPage, BlogPage
from project.models import ProjectIndexPage, ProjectPage
from experience.models import ExperienceIndexPage, ExperiencePage
from misc.models import MiscPage


class HomePage(Page):
    max_count = 1

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    summary = models.TextField(blank=True, max_length=500)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cta_url = models.URLField(blank=True)

    my_story_title = models.CharField(
        max_length=40, blank=True, default="My Story"
    )
    my_story_content = models.TextField(blank=True, max_length=800)

    content_panels = Page.content_panels + [
        FieldPanel("author_image"),
        FieldPanel("summary"),
        FieldPanel("cta_text"),
        FieldPanel("cta_page"),
        FieldPanel("cta_url"),
        MultiFieldPanel(
            [
                FieldPanel("my_story_title"),
                FieldPanel("my_story_content"),
            ],
            heading="My Story",
        ),
    ]

    @property
    def cta_link(self):
        if self.cta_page:
            return self.cta_page.url
        elif self.cta_url:
            return self.cta_url
        return None

    @property
    def button_text(self):
        return self.cta_text or "Read More"

    def get_context(self, request):
        context = super().get_context(request)
        context["blog_index"] = BlogIndexPage.objects.first()
        context["blog_posts"] = (
            BlogPage.objects.live()
            .public()
            .order_by("-first_published_at")[:3]
        )
        context["project_index"] = ProjectIndexPage.objects.first()
        context["projects"] = (
            ProjectPage.objects.live()
            .public()
            .order_by("-first_published_at")[:3]
        )
        context["experience_index"] = ExperienceIndexPage.objects.first()
        context["experiences"] = (
            ExperiencePage.objects.live()
            .public()
            .order_by("-first_published_at")[:2]
        )
        if misc_page := MiscPage.objects.first():
            context["skills"] = misc_page.skill.all()[:5]
        else:
            context["skills"] = []
        return context
