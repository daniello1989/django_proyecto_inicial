# Generated by Django 3.2.23 on 2023-11-09 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0003_autor_biografia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poema',
            name='autor',
        ),
    ]
