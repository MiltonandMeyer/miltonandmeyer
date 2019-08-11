from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock, CharBlock, URLBlock
from wagtail.documents.blocks import DocumentChooserBlock
import home.blocks as cblocks
from wagtail.admin.edit_handlers import StreamFieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class NavigationMenuBarSettings(BaseSetting):
    menu = StreamField([('internal_link_block', cblocks.InternalLinkBlock()),])
    main_welcome_page = models.ForeignKey(
            'wagtailcore.Page',
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name='+',
    )

    panels = [
    PageChooserPanel('main_welcome_page'),
    StreamFieldPanel('menu'),
    ]

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL', blank=True)
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @', blank=True)
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL', blank=True)
    twitter = models.CharField(
        max_length=255, help_text='Your twitter handle, without the @', blank=True)


@register_setting
class SiteFooterSettings(BaseSetting):
    left_column = StreamField([('internal_link_block', cblocks.InternalLinkBlock()),
                                ('external_link_block', cblocks.ExternalLinkBlock()),
                                ('short_text', CharBlock(max_length=300)),
                                ('external_document', DocumentChooserBlock()),
    ])
    middle_column = StreamField([('internal_link_block', cblocks.InternalLinkBlock()),
                                ('external_link_block', cblocks.ExternalLinkBlock()),
                                ('short_text', CharBlock(max_length=300)),
                                ('external_document', DocumentChooserBlock()),
    ])
    right_column = StreamField([('internal_link_block', cblocks.InternalLinkBlock()),
                                ('external_link_block', cblocks.ExternalLinkBlock()),
                                ('short_text', CharBlock(max_length=300)),
                                ('external_document', DocumentChooserBlock()),
    ])

    panels = [
        StreamFieldPanel('left_column'),
        StreamFieldPanel('middle_column'),
        StreamFieldPanel('right_column'),
    ]


@register_setting
class SiteStyleSettings(BaseSetting):
    style = StreamField([('styles', cblocks.SiteThemeBlock())], blank=True);

    panels = [
        StreamFieldPanel('style'),
    ]
