# Generated by Django 4.2.2 on 2023-06-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='report_count',
            field=models.IntegerField(default=0),
        ),
    ]
