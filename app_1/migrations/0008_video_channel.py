# Generated by Django 4.2.dev20221024115451 on 2022-11-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_remove_channel_user_comment_datetime_comment_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.channel'),
        ),
    ]
