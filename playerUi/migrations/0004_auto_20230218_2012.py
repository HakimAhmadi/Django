# Generated by Django 3.2.13 on 2023-02-18 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerUi', '0003_auto_20230218_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_file',
        ),
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
    ]
