# Generated by Django 2.0.2 on 2018-04-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20180413_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='text',
            field=models.TextField(verbose_name=' '),
        ),
    ]
