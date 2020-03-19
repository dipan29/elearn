# Generated by Django 2.2 on 2020-03-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_pageinfo_vimeo_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_title', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('thumbnail', models.ImageField(blank=True, help_text='This field expects an user image file, 480x360 is ideal', upload_to='testimonials/')),
            ],
        ),
    ]