# Generated by Django 2.0.1 on 2018-01-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_auto_20180122_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
