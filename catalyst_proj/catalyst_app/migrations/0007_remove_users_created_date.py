# Generated by Django 5.1.2 on 2024-10-20 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst_app', '0006_company_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='created_date',
        ),
    ]
