# Generated by Django 3.1.3 on 2020-11-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0002_auto_20201114_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenerurl',
            name='short_url',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
