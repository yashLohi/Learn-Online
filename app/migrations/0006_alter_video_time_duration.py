# Generated by Django 4.0.8 on 2023-11-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time_duration',
            field=models.IntegerField(null=True),
        ),
    ]
