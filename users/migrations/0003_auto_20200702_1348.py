# Generated by Django 2.0 on 2020-07-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200629_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
    ]
