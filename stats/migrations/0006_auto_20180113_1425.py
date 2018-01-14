# Generated by Django 2.0.1 on 2018-01-13 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20180113_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='stats.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='stats.Team'),
        ),
    ]
