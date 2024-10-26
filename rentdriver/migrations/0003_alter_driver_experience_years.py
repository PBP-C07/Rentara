# Generated by Django 5.1.2 on 2024-10-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentdriver', '0002_remove_driver_is_available_delete_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='experience_years',
            field=models.CharField(choices=[('2+', '2+ Years'), ('5+', '5+ Years'), ('7+', '7+ Years'), ('10+', '10+ Years')], default='2+', max_length=3),
        ),
    ]
