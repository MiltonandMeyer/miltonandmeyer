# Generated by Django 2.2.3 on 2019-08-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190810_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='blog_title',
            field=models.CharField(default='Blank Title', max_length=250),
            preserve_default=False,
        ),
    ]