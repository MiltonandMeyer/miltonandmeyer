from wagtail.core.blocks import StructBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.db import models
from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField, StreamField

class SiteThemeBlock(StructBlock):
    BLUE = '87,144,212'
    GREEN = '86,207,140'
    RUSTY = '146,89,20'
    GREY = '90,105,120'
    NONE = '255,255,255'
    COLOUR_CHOICES = (
    (BLUE, 'Blue'),
    (GREEN, 'Green'),
    (RUSTY, 'Rusty Red/Orange'),
    (GREY, 'Grey'),
    (NONE, 'None'),
    )
    site_colour = blocks.ChoiceBlock(choices=COLOUR_CHOICES, help_text="Pick a colour",)
    site = blocks.PageChooserBlock()
    site_image = ImageChooserBlock()
    site_blurb = blocks.RichTextBlock()


class ExternalLinkBlock(StructBlock):
    external_link = blocks.URLBlock()
    link_text = blocks.CharBlock(max_length=255)

class InternalLinkBlock(StructBlock):
    internal_link = blocks.PageChooserBlock();
    link_text = blocks.CharBlock(max_length=255)

class HeadingandSubHeadingBlock(StructBlock):
    heading = blocks.CharBlock()
    subheading = blocks.CharBlock(required=False)

    class Meta:
        template = "home/Heading-and-Subheading-Block.html"

class ArticlePreviewBlock(StructBlock):
    title = blocks.CharBlock(classname="full title")
    excerpt = blocks.RichTextBlock()
    image = ImageChooserBlock()
    link_page = blocks.PageChooserBlock()

    class Meta:
        icon = "cogs"
        template = "home/Article-Preview-Block.html"

class TextImageBlock(StructBlock):
    title = blocks.CharBlock(required=False, classname="full title")
    text = blocks.RichTextBlock()
    image = ImageChooserBlock()
    link_page = blocks.PageChooserBlock(required=False, blank=True)

    class Meta:
        icons = "cogs"
        template = "home/Text-Image-Block.html"

class ThreeColumnBlock(StructBlock):
    first_column = TextImageBlock()
    second_column = TextImageBlock()
    third_column = TextImageBlock()

    class Meta:
        template = "home/Three-Column-Block.html"

#class BlogIndexBlock(StructBlock):
#    intro = RichTextField(blank=True)
#    content_panels = Page.content_panels + [FieldPanel('intro', classname='full')]

#    def get_context(self, request):
#        context=super().get_context(request)
#        blogpages=self.get_children().live().order_by('-first_published_at')
#        context['blogpages']= blogpages
#        return context

# BLUE = '87,144,212'
# GREEN = '86,207,140'
# RUSTY = '146,89,20'
# GREY = '90,105,120'
# NONE = '255,255,255'
# COLOUR_CHOICES = (
# (BLUE, 'Blue'),
# (GREEN, 'Green'),
# (RUSTY, 'Rusty Red/Orange'),
# (GREY, 'Grey'),
# (NONE, 'None'),
# )
# site_colour_theme = models.CharField(
#     max_length=11,
#     choices=COLOUR_CHOICES,
#     default=NONE,
#     help_text="Pick a colour"
# )
# site_banner_image = models.ForeignKey(
#     'wagtailimages.Image',
#     null=True,
#     blank=True,
#     on_delete=models.CASCADE, #models.SET_NULL
#     related_name='+',
# )
#
# panels = [
#     ImageChooserPanel('site_banner_image'),
#     FieldPanel('site_colour_theme'),
# ]
