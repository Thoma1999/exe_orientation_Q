# Generated by Django 2.1.15 on 2020-03-05 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200305_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]
