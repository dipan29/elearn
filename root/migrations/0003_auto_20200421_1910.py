# Generated by Django 2.2 on 2020-04-21 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_discount_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Category'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]