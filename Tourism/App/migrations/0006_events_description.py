# Generated by Django 4.2.6 on 2023-11-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]