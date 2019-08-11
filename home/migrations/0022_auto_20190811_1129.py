# Generated by Django 2.2.3 on 2019-08-11 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0021_auto_20190811_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='site',
        ),
        migrations.AddField(
            model_name='homepage',
            name='bottom_left_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bottom_right_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
