# Generated by Django 4.0.3 on 2022-04-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_custompage_show_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='caption_left',
            field=models.BooleanField(default=False),
        ),
    ]