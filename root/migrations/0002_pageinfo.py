# Generated by Django 2.2 on 2020-03-18 20:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField(help_text='Enter about Information for the Website as normal Word Doc')),
                ('contact', ckeditor.fields.RichTextField(help_text='Enter Contact like email phone address like normal page')),
                ('services', ckeditor.fields.RichTextField(help_text='Enter the range of services provided to users by Insta Worthy Academy')),
                ('facebook_link', models.CharField(blank=True, max_length=300)),
                ('twitter_link', models.CharField(blank=True, max_length=300)),
                ('instagram_link', models.CharField(blank=True, max_length=300)),
                ('youtube_link', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'PageInfo',
                'verbose_name_plural': 'PageInfo(s)',
            },
        ),
    ]
