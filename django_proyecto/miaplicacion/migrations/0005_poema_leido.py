# Generated by Django 3.2.23 on 2023-11-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0004_remove_poema_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='poema',
            name='leido',
            field=models.BooleanField(default=False),
        ),
    ]
