# Generated by Django 3.0 on 2020-12-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20201012_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(choices=[(1, '合ってる(8割)'), (2, '概ね合ってる（6割）'), (3, 'あまり合っていない（４割）'), (4, '合ってない(４割以下)'), (5, 'その他・コメント')], default=None, verbose_name='正答率'),
        ),
    ]
