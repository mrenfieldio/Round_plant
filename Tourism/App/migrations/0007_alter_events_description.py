# Generated by Django 4.2.6 on 2023-11-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_events_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
