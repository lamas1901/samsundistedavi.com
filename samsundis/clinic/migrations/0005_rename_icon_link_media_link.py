# Generated by Django 4.0.3 on 2022-04-04 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='icon_link',
            new_name='link',
        ),
    ]