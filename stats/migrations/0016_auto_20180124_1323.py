# Generated by Django 2.0.1 on 2018-01-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0015_auto_20180124_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
