from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from django.db import models
from wagtail.search import index
from modelcluster.fields import ParentalKey
import home.blocks as cblocks
import home.settings

from wagtail.contrib.settings.models import BaseSetting, register_setting


class HomePage(Page):
    center_field = models.ForeignKey(
            'wagtailcore.Page',
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name='+',
    )
    site_styles = StreamField([
                    ('top_left_site', cblocks.SiteThemeBlock()),
    ], blank=True);



    about = StreamField([('image', ImageChooserBlock()),
                        ('dark_block_heading', cblocks.HeadingandSubHeadingBlock(classname='full title')),
                        ('paragraph_text', blocks.RichTextBlock()),
                        ('article_preview', cblocks.ArticlePreviewBlock()),
                        ('words_and_images', cblocks.TextImageBlock()),
                        ('video', EmbedBlock()),
                        ('three_column_content', cblocks.ThreeColumnBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('center_field'),
        StreamFieldPanel('site_styles'),
        StreamFieldPanel('about'),
    ]

class BlogPage(Page):
    date=models.DateField("Post date")
    blog_title=models.CharField(max_length=250)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank="True")
    author = models.CharField(max_length=250)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            ], heading="Blog Information"),
        FieldPanel('author'),
        FieldPanel('intro'),
        FieldPanel('body', classname='full'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogIndexPage(Page):
   intro = RichTextField(blank=True)

   def get_context(self, request): #update context to include only published posts and order reverse chron
       context=super().get_context(request)
       blogpages=self.get_children().live().order_by('-first_published_at')
       context['blogpages']= blogpages
       return context

class BlogPageGalleryImage(Orderable):
    page=ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=250)

    panels = [ImageChooserPanel('image'),
              FieldPanel('caption'),
              ]

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogTagIndexPage(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class StandardPage(Page):
    #date = models.DateField("Publishing Date")
    body = StreamField([('image', ImageChooserBlock()),
                        ('dark_block_heading', cblocks.HeadingandSubHeadingBlock(classname='full title')),
                        ('paragraph_text', blocks.RichTextBlock()),
                        ('article_preview', cblocks.ArticlePreviewBlock()),
                        ('words_and_images', cblocks.TextImageBlock()),
                        ('video', EmbedBlock()),
                        ('three_column_content', cblocks.ThreeColumnBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
