# Generated by Django 2.0.13 on 2019-02-21 22:11

from django.db import migrations, models
import drf_starter.the_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data',
            field=models.ImageField(null=True, upload_to=drf_starter.the_app.models.get_uuid),
        ),
    ]
