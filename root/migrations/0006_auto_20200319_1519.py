# Generated by Django 2.2 on 2020-03-19 09:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_pageinfo_linkedin_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageinfo',
            name='privacy_policy',
            field=ckeditor.fields.RichTextField(default='privacy', help_text='Enter the Terms and Condition'),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='tnc',
            field=ckeditor.fields.RichTextField(default='tnc', help_text='Enter the Terms and Condition'),
        ),
    ]