# Generated by Django 4.2.5 on 2023-09-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_remove_tariff_price_tariff_main_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='badge_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Акционные условия'),
        ),
    ]