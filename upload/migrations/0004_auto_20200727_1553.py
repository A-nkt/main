# Generated by Django 3.0.8 on 2020-07-27 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('upload', '0003_auto_20200726_2159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
