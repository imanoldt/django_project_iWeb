# Generated by Django 4.1.3 on 2022-11-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0004_comment_remove_user_edad_video_duracion_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="channel_name",
            new_name="title",
        ),
        migrations.RenameField(
            model_name="video",
            old_name="duracion",
            new_name="length",
        ),
    ]
