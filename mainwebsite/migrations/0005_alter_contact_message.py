# Generated by Django 4.1.6 on 2023-04-06 11:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0004_rename_achievements_achievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
