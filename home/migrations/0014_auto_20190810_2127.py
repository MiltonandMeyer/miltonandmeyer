# Generated by Django 2.2.3 on 2019-08-10 21:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190810_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitefootersettings',
            name='left_column',
            field=wagtail.core.fields.StreamField([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('external_link', wagtail.core.blocks.URLBlock()), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
        migrations.AlterField(
            model_name='sitefootersettings',
            name='middle_column',
            field=wagtail.core.fields.StreamField([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('external_link', wagtail.core.blocks.URLBlock()), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
        migrations.AlterField(
            model_name='sitefootersettings',
            name='right_column',
            field=wagtail.core.fields.StreamField([('internal_link', wagtail.core.blocks.PageChooserBlock()), ('external_link', wagtail.core.blocks.URLBlock()), ('short_text', wagtail.core.blocks.CharBlock(max_length=300)), ('external_document', wagtail.documents.blocks.DocumentChooserBlock())]),
        ),
    ]
