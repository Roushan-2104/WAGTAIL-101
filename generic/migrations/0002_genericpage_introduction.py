# Generated by Django 3.2.9 on 2021-11-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
    ]
