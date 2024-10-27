# Generated by Django 5.1.2 on 2024-10-25 13:08

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
            name='Reviews',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('helpful_votes', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
