# Generated by Django 2.2 on 2020-03-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_pageinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageinfo',
            name='vimeo_link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]