# Generated by Django 5.2.3 on 2025-07-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
