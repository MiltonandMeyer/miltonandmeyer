# Generated by Django 2.2.3 on 2019-08-03 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_socialmediasettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardpage',
            name='date',
        ),
        migrations.DeleteModel(
            name='SocialMediaSettings',
        ),
    ]
