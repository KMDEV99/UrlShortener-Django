# Generated by Django 3.1.3 on 2020-11-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0004_shortenerurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenerurl',
            name='short_url',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
