# Generated by Django 3.2.13 on 2023-02-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerUi', '0004_auto_20230218_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album_title',
        ),
        migrations.RemoveField(
            model_name='song',
            name='email',
        ),
        migrations.RemoveField(
            model_name='song',
            name='is_album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='note',
        ),
    ]