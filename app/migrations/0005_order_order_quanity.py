# Generated by Django 5.1.5 on 2025-01-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cartitem_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_quanity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
