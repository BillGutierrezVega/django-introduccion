# Generated by Django 4.1.7 on 2023-11-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelage', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='car',
            field=models.ManyToManyField(to='modelage.car', verbose_name='los carros del usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='el nombre del usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='el apellido del usuario'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
