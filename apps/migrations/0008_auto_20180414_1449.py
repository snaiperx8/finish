# Generated by Django 2.0.2 on 2018-04-14 11:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20180414_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name=False),
        ),
    ]