# Generated by Django 3.0.8 on 2020-07-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0004_auto_20200727_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='year',
            field=models.IntegerField(default=2019, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='past/', verbose_name='過去問'),
        ),
    ]
