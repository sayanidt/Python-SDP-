from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget - ₹{self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True)  # Add this to link with Budget

def __str__(self):
        return f"{self.description} - {self.amount} "


class Transaction(models.Model):
        # Choices for transaction type
        TRANSACTION_TYPES = (
            ('Income', 'Income'),
            ('Expense', 'Expense'),
        )

        # Model Fields
        date = models.DateField(default=timezone.now)  # Automatically sets the current date
        description = models.CharField(max_length=255)  # Description of the transaction
        category = models.CharField(max_length=100)  # Transaction category (e.g., groceries, salary)
        transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Income or Expense
        amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount


def __str__(self):
    return f"{self.date} - {self.description} ({self.transaction_type})"



