# Generated by Django 3.2.23 on 2023-11-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0006_autor_leido'),
    ]

    operations = [
        migrations.AddField(
            model_name='poema',
            name='guardado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poema',
            name='megusta',
            field=models.IntegerField(default=0),
        ),
    ]
