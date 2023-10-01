# Generated by Django 4.2.4 on 2023-10-01 14:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_service_service_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_header',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='service',
            name='service_img',
            field=models.ImageField(default='', upload_to='service_photo'),
        ),
    ]
