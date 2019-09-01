# Generated by Django 2.2.3 on 2019-09-01 16:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_sitestylesettings_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='site_style',
            field=wagtail.core.fields.StreamField([('site_theme', wagtail.core.blocks.StructBlock([('site_colour', wagtail.core.blocks.ChoiceBlock(choices=[('87,144,212', 'Blue'), ('86,207,140', 'Green'), ('146,89,20', 'Rusty Red/Orange'), ('90,105,120', 'Grey'), ('255,255,255', 'None')], help_text='Pick a colour')), ('site', wagtail.core.blocks.PageChooserBlock()), ('site_image', wagtail.images.blocks.ImageChooserBlock()), ('site_blurb', wagtail.core.blocks.RichTextBlock())]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='site_styles',
            field=wagtail.core.fields.StreamField([('one_site_area', wagtail.core.blocks.StructBlock([('site_colour', wagtail.core.blocks.ChoiceBlock(choices=[('87,144,212', 'Blue'), ('86,207,140', 'Green'), ('146,89,20', 'Rusty Red/Orange'), ('90,105,120', 'Grey'), ('255,255,255', 'None')], help_text='Pick a colour')), ('site', wagtail.core.blocks.PageChooserBlock()), ('site_image', wagtail.images.blocks.ImageChooserBlock()), ('site_blurb', wagtail.core.blocks.RichTextBlock())]))], blank=True),
        ),
    ]