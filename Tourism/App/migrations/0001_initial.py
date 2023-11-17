# Generated by Django 4.2.6 on 2023-11-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('duriation', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='img')),
            ],
        ),
    ]