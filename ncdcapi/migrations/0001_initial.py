# Generated by Django 4.0.4 on 2022-04-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='state_distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_infected', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('Latitude_value', models.CharField(max_length=200)),
                ('Latitude_alias', models.CharField(max_length=200)),
                ('Longitude_value', models.CharField(max_length=200)),
                ('Longitude_alias', models.CharField(max_length=200)),
            ],
        ),
    ]
