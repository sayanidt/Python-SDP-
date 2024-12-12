from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Expense, Budget, Transaction

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Expense Form
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description']

# Budget Form
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'transaction_type', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
                }

