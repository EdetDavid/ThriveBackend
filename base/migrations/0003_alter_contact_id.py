# Generated by Django 4.0.5 on 2023-01-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221218_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
