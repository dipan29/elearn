# Generated by Django 2.2 on 2020-03-12 16:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200312_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
