# Generated by Django 3.0.8 on 2020-07-28 10:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200728_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add news title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.CharBlock(help_text='Add news link', required=True))]))], blank=True, null=True),
        ),
    ]
