# Generated by Django 5.1.2 on 2024-10-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewajual', '0002_alter_vehicle_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['merk', 'tipe'], 'verbose_name': 'Kendaraan', 'verbose_name_plural': 'Daftar Kendaraan'},
        ),
    ]