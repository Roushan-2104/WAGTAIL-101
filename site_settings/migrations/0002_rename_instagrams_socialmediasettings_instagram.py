# Generated by Django 3.2.9 on 2021-11-11 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediasettings',
            old_name='instagrams',
            new_name='instagram',
        ),
    ]
