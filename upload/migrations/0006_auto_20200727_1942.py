# Generated by Django 3.0.8 on 2020-07-27 10:42

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20200727_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='Page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='upload.UploadPage'),
        ),
    ]
