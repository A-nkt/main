# Generated by Django 3.0.8 on 2020-07-30 01:51

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_remove_aboutpage_about_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True)), ('text', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True))]))], blank=True, null=True),
        ),
    ]
