# Generated by Django 5.0.7 on 2024-07-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
