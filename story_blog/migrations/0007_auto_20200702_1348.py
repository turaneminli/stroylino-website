# Generated by Django 2.0 on 2020-07-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_blog', '0006_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=28),
        ),
    ]