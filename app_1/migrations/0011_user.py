# Generated by Django 4.2.dev20221024115451 on 2022-11-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0010_delete_user_video_likes_alter_comment_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]