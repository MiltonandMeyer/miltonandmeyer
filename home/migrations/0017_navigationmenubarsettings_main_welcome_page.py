# Generated by Django 2.2.3 on 2019-08-11 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0016_auto_20190811_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationmenubarsettings',
            name='main_welcome_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]