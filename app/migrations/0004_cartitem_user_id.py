# Generated by Django 5.1.5 on 2025-01-26 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customuser_email_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
