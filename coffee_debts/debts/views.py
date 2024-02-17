from django.shortcuts import render
from django.http import JsonResponse
from .models import Person, CoffeePurchase
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoffeePurchaseForm, CreateUserForm
from .models import CoffeePurchase, Person 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import CoffeePurchase
from .forms import CoffeePurchaseForm
from .models import UserDebtSummary, Debt
# from .forms import BatchCoffeePurchaseForm
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models import Sum, F
from .models import UserDebtSummary
from .utils import pay_coffee_for_all
from .forms import CoffeeCostForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST" :
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, '../templates/debts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created successfully for ' + user)
                
                return redirect('login')
                
        context = {'form': form}
        return render(request, '../templates/debts/register.html', context)
    
def about_page(request):
    form = CoffeeCostForm()
    return render(request, 'debts/about.html')

@login_required(login_url='login')
def home_page(request):
    return render(request, 'debts/base.html')

@login_required(login_url='login')
def add_coffee_purchase(request):
    if request.method == 'POST':
        form = CoffeePurchaseForm(request.POST)
        if form.is_valid():
            coffee_purchase = form.save(commit=False)
            coffee_purchase.user = request.user
            coffee_purchase.save()

            # Update UserDebtSummary
            debt_summary, created = UserDebtSummary.objects.get_or_create(user=request.user)
            debt_summary.total_debt += coffee_purchase.cost 
            debt_summary.save()

            return redirect('home')
    else:
        form = CoffeePurchaseForm()
    return render(request, 'debts/base.html', {'form': form})

def list_debts(request):
    users_debts = UserDebtSummary.objects.all()
    return render(request, 'debts/list_debts.html', {'users_debts': users_debts})

class SignUpView(generic.CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'
        
@login_required(login_url='login')
def coffee_debt_summary(request):
    message = pay_coffee_for_all()  # Adjust this function to return a message instead of printing
    return render(request, 'debts/about.html', {'message': message})

@login_required(login_url='login')
def add_coffee_costs(request):
    if request.method == 'POST':
        form = CoffeeCostForm(request.POST)
        if form.is_valid():
            costs = {field.replace('_cost', ''): form.cleaned_data[field] for field in form.fields if form.cleaned_data[field] is not None}
            total_cost = sum(costs.values())

            # Identify the user with the highest debt
            highest_debtor = UserDebtSummary.objects.order_by('-total_debt').first()

            if highest_debtor:
                # Subtract the cost of the highest debtor's coffee from the total, if applicable
                highest_debtor_coffee_cost = costs.pop(highest_debtor.user.username, 0)
                total_cost -= highest_debtor_coffee_cost

                highest_debtor.total_debt -= total_cost
                highest_debtor.save()

                for username, cost in costs.items():
                    user = User.objects.get(username=username)
                    try:
                        user_debt_summary = UserDebtSummary.objects.get(user=user)
                        user_debt_summary.total_debt += cost
                        user_debt_summary.save()
                    except UserDebtSummary.DoesNotExist:
                        UserDebtSummary.objects.create(user=user, total_debt=cost)

                message = f"{highest_debtor.user.username}'s debt adjusted by {total_cost}, other debts updated."
            else:
                message = "No debts found to process."

            return render(request, 'debts/about.html', {'message': message})
    else:
        form = CoffeeCostForm()
        
    return render(request, 'debts/about.html', {'form': form})