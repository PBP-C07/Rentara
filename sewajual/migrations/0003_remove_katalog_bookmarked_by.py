# Generated by Django 5.1.2 on 2024-10-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewajual', '0002_remove_katalog_owner_katalog_bookmarked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katalog',
            name='bookmarked_by',
        ),
    ]
