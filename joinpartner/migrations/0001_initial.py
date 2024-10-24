# Generated by Django 5.1.2 on 2024-10-19 04:42

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
            name='Partner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=255)),
                ('gmaps_link', models.URLField(max_length=500)),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_image', models.URLField()),
                ('brand', models.CharField(max_length=100)),
                ('brand_type', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('tersedia', 'Tersedia'), ('tidak tersedia', 'Tidak Tersedia')], default='tersedia', max_length=15)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='joinpartner.partner')),
            ],
        ),
    ]
