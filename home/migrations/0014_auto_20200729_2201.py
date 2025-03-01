# Generated by Django 3.0.8 on 2020-07-29 13:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_homepage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='news',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='news_link',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, help_text='Add news title', max_length=100, null=True)), ('link', wagtail.core.blocks.CharBlock(blank=True, help_text='Add news link', max_length=100, null=True))]))], blank=True, null=True),
        ),
    ]
