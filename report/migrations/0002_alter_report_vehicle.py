# Generated by Django 5.1.2 on 2024-10-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='vehicle',
            field=models.CharField(max_length=255),
        ),
    ]
