# Generated by Django 3.0.8 on 2020-07-11 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story_blog', '0009_commentnotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentnotification',
            old_name='userID',
            new_name='user',
        ),
    ]