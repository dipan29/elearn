# Generated by Django 2.2 on 2020-04-21 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Category'),
        ),
    ]
