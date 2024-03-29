# Generated by Django 5.0.2 on 2024-02-16 08:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0003_debt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeepurchase',
            old_name='buyer',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='coffeepurchase',
            name='date',
        ),
        migrations.AddField(
            model_name='coffeepurchase',
            name='date_purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='coffeepurchase',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='Enter the cost of the coffee', max_digits=6),
        ),
    ]
