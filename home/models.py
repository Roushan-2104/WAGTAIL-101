from django.db import models
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default='Welcome To My HomePage !!')
    
    banner_image_home = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False, 
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField([
        ('heading', blocks.CharBlock(template="heading_block.html")),
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ],null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image_home"),
        StreamFieldPanel("body"),
    ]