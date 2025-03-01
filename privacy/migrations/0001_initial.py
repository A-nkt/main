# Generated by Django 3.0 on 2020-10-11 16:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('rule_content', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about title', max_length=100, null=True)), ('text', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True))])), ('date', wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add your Date', max_length=1000, null=True))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
