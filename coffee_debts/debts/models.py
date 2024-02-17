from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)


# class CoffeePurchase(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Enter the cost of the coffee")
#     date_purchased = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         # Corrected to use self.cost instead of self.amount
#         return f"{self.user.username} - ${self.cost} on {self.date_purchased.strftime('%Y-%m-%d')}"
class CoffeePurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Enter the cost of the coffee")
    date_purchased = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date_purchased}"
    
class Debt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    field=models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return f"{self.description} - {self.amount} owed by {self.user.username}"

class UserDebtSummary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='debt_summary')
    total_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Total Debt: {self.total_debt}"
    