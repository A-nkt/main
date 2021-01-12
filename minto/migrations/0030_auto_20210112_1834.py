# Generated by Django 3.0 on 2021-01-12 09:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('minto', '0029_auto_20210103_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentspage',
            name='VALUE',
            field=wagtail.core.fields.StreamField([('INDEX', wagtail.core.blocks.StructBlock([('research_name', wagtail.core.blocks.CharBlock(blank=True, help_text='研究科名', max_length=100, null=True)), ('IDname', wagtail.core.blocks.CharBlock(blank=True, default='Chart', help_text='IDname', max_length=100, null=True)), ('RinkID', wagtail.core.blocks.CharBlock(blank=True, help_text='RinkID', max_length=100, null=True)), ('int0', wagtail.core.blocks.IntegerBlock(blank=True, help_text='500点以下', null=True)), ('int1', wagtail.core.blocks.IntegerBlock(blank=True, help_text='500~600点', null=True)), ('int2', wagtail.core.blocks.IntegerBlock(blank=True, help_text='600~700点', null=True)), ('int3', wagtail.core.blocks.IntegerBlock(blank=True, help_text='700~800点', null=True)), ('int4', wagtail.core.blocks.IntegerBlock(blank=True, help_text='800~900点', null=True)), ('int5', wagtail.core.blocks.IntegerBlock(blank=True, help_text='900点以上', null=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentspage',
            name='mintopage_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='minto.MintoPage'),
        ),
    ]
