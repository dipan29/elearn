# Generated by Django 2.2 on 2020-04-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200320_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='are_you_a_social_media_marketeer',
        ),
        migrations.AddField(
            model_name='user',
            name='are_you_a_brand',
            field=models.BooleanField(default=False),
        ),
    ]
