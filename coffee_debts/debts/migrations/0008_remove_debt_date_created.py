# Generated by Django 5.0.2 on 2024-02-17 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0007_remove_coffeepurchase_purchase_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='date_created',
        ),
    ]