# Generated by Django 2.2.5 on 2019-09-06 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_map_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='map',
            options={'ordering': ['-date']},
        ),
    ]
