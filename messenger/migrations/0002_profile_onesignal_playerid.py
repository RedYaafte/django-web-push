# Generated by Django 2.2.3 on 2019-07-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='onesignal_playerId',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
