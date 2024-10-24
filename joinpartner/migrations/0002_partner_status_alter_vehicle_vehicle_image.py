# Generated by Django 5.1.1 on 2024-10-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joinpartner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_image',
            field=models.URLField(max_length=500),
        ),
    ]