# Generated by Django 4.1.2 on 2022-12-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0013_video_dislikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('description', models.CharField(max_length=300, null=True)),
                ('cathegory', models.CharField(choices=[('1', 'COMIDA'), ('2', 'DEPORTE'), ('3', 'ENTRETENIMIENTO'), ('4', 'OCIO'), ('5', 'SERIE'), ('6', 'VIAJES'), ('7', 'BUSINESS')], default='', max_length=300, null=True)),
                ('file', models.FileField(null=True, upload_to='videos')),
            ],
        ),
    ]
