from django.shortcuts import render, redirect
from django.utils import timezone
from collections import defaultdict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget, Transaction
from .forms import UserRegistrationForm, ExpenseForm, BudgetForm, TransactionForm
from django.contrib import messages
from django.db.models import Sum
from .models import Expense, Transaction
from django.http import HttpResponse



# Home Page
def home(request):
    return render(request, 'home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Budget View
@login_required
def budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'Budget set successfully!')
    else:
        form = BudgetForm()
    budget = Budget.objects.filter(user=request.user).last()
    return render(request, 'budget.html', {'form': form, 'budget': budget})

# Expense Entry
@login_required
def expenses(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
    else:
        form = ExpenseForm()
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses.html', {'form': form, 'expenses': expenses})

# Weekly Summary
@login_required
def summary(request):
    # Assuming you already have budget and total_spent variables
    budget = 1000  # Replace with your actual budget logic
    total_spent = 400  # Replace with your actual spent logic

    # Calculate percentage
    if budget > 0:
        percentage_spent = (total_spent / budget) * 100
    else:
        percentage_spent = 0

    context = {
        'budget': budget,
        'total_spent': total_spent,
        'percentage_spent': round(percentage_spent),  # round to make it cleaner
    }

    return render(request, 'summary.html', context)


# Expense Analysis
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

@login_required
def analysis(request):
    # Example data (Replace with actual database queries)
    expenses = [
        {'category': 'Food', 'amount': 5000},
        {'category': 'Transport', 'amount': 2000},
        {'category': 'Rent', 'amount': 12000},
        {'category': 'Entertainment', 'amount': 3000},
    ]

    # Extract categories and amounts
    categories = [expense['category'] for expense in expenses]
    amounts = [expense['amount'] for expense in expenses]

    # Pass data to the template in JSON format
    context = {
        'categories': json.dumps(categories),
        'amounts': json.dumps(amounts),
    }
    return render(request, 'analysis.html', context)

def transactions(request):
    transactions = Transaction.objects.all().order_by('-date')  # Fetch all transactions, newest first

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions')  # Reload the page after adding transaction
    else:
        form = TransactionForm()

    total_income = sum(t.amount for t in transactions if t.transaction_type == 'Income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'Expense')
    total_balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'form': form,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance,
    }

    return render(request, 'transactions.html', context)

def chatbot(request):
    return render(request, 'chatbot.html')
