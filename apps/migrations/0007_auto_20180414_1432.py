# Generated by Django 2.0.2 on 2018-04-14 11:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20180413_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name=' '),
        ),
    ]