# Generated by Django 2.2 on 2020-03-12 15:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200312_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=ckeditor.fields.RichTextField(default='Unset'),
        ),
    ]
