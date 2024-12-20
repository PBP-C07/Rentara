# Generated by Django 5.1.2 on 2024-10-27 04:01

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('rental_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('issue_type', models.CharField(choices=[('mismatch', 'Kendaraan tidak sesuai merek yang dipesan'), ('damaged', 'Kendaraan rusak'), ('service', 'Pelayanan tidak ramah')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='report.vehicle')),
            ],
        ),
    ]
