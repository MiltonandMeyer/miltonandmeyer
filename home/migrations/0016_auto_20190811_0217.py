# Generated by Django 2.2.3 on 2019-08-11 02:17

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0015_auto_20190810_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitefootersettings',
            name='left_column',
            field=wagtail.core.fields.StreamField([('internal_link_block', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('external_link_block', wagtail.core.blocks.StructBlock([('external_link', wagtail.core.blocks.URLBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
        migrations.AlterField(
            model_name='sitefootersettings',
            name='middle_column',
            field=wagtail.core.fields.StreamField([('internal_link_block', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('external_link_block', wagtail.core.blocks.StructBlock([('external_link', wagtail.core.blocks.URLBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
        migrations.AlterField(
            model_name='sitefootersettings',
            name='right_column',
            field=wagtail.core.fields.StreamField([('internal_link_block', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('external_link_block', wagtail.core.blocks.StructBlock([('external_link', wagtail.core.blocks.URLBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))])), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('dark_block_heading', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('subheading', wagtail.core.blocks.CharBlock(required=False))], classname='full title')), ('paragraph_text', wagtail.core.blocks.RichTextBlock()), ('article_preview', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title')), ('excerpt', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link_page', wagtail.core.blocks.PageChooserBlock())])), ('words_and_images', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock()), ('three_column_content', wagtail.core.blocks.StructBlock([('first_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('second_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('third_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))]),
        ),
        migrations.CreateModel(
            name='NavigationMenuBarSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', wagtail.core.fields.StreamField([('internal_link_block', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(max_length=255))]))])),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
