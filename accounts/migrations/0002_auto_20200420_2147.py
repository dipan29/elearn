# Generated by Django 2.2 on 2020-04-20 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='average_SGPA_till_last_published_semester',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='user',
            name='class_12_mark_in_percentage',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_year_of_BTech',
            field=models.CharField(choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')], default=2022, max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='name_of_your_college',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsApp_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='your_deparment_of_study',
            field=models.CharField(blank=True, choices=[('ECE', 'ECE'), ('EEE/EE', 'EEE/EE'), ('AEIE', 'AEIE'), ('CSE', 'CSE'), ('IT', 'IT'), ('ME', 'ME'), ('CE', 'CE'), ('CHEM', 'CHEM'), ('BT', 'BT'), ('FT', 'FT'), ('OTHER', 'OTHER')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
