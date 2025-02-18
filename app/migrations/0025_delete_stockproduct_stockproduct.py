# Generated by Django 4.2.3 on 2025-02-12 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_delete_stockproduct_stockproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockProduct',
        ),
        migrations.CreateModel(
            name='StockProduct',
            fields=[
            ],
            options={
                'verbose_name': 'Stock Product',
                'verbose_name_plural': 'Stock\xa0Products',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.product',),
        ),
    ]
