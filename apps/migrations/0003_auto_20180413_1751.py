# Generated by Django 2.0.2 on 2018-04-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20180405_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='text',
            field=models.TextField(),
        ),
    ]
