# Generated by Django 5.1.4 on 2025-04-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_course_remove_video_channel_remove_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
