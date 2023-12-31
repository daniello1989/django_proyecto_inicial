# Generated by Django 3.2.23 on 2023-11-15 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miaplicacion', '0008_proyecto_megusta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=1)),
                ('nombre', models.CharField(default='', max_length=200)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='poema',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miaplicacion.autor'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miaplicacion.autor'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]
