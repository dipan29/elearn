# Generated by Django 2.2 on 2020-03-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_pageinfo_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageinfo',
            name='contact_number',
            field=models.CharField(blank=True, help_text='Enter your contact number', max_length=14),
        ),
    ]
