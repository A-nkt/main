# Generated by Django 3.1.5 on 2021-01-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minto_contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='clean_name',
            field=models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name'),
        ),
    ]
