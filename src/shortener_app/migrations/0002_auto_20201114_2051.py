# Generated by Django 3.1.3 on 2020-11-14 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortenerurl',
            old_name='timestamp',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='shortenerurl',
            old_name='shortcode',
            new_name='short_url',
        ),
    ]