# Generated by Django 3.0 on 2020-12-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans_upload', '0005_auto_20201204_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to='past/', verbose_name='過去問解答'),
        ),
    ]
