# Generated by Django 2.0.1 on 2018-01-24 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0014_auto_20180123_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-win']},
        ),
    ]
