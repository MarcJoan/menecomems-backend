# Generated by Django 3.1.7 on 2021-03-23 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0003_auto_20210323_1940'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Robots',
            new_name='Robot',
        ),
    ]