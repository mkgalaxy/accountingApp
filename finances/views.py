from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction, UserProfile
from .forms import TransactionForm, UserProfileForm
def welcome_view(request):
    return render(request, 'finances/welcome.html')
#------------------------------------------------------------------------------------------------------
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # احراز هویت موفق
            user = form.get_user()
            login(request, user)
            # پس از ورود موفق، کاربر را به داشبورد هدایت می‌کنیم
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'finances/login.html', context)
#------------------------------------------------------------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('login')
#------------------------------------------------------------------------------------------------------
@login_required
def dashboard_view(request):
    if request.user.is_superuser: # اگر ادمین کل بود
        transactions = Transaction.objects.all()
    else: # اگر یوزر معمولی حسابداری بود
        transactions = Transaction.objects.filter(user=request.user)
    context = {
        'transactions': transactions,
    }
    return render(request, 'finances/dashboard.html', context)
#------------------------------------------------------------------------------------------------------
@login_required # انجام تراکنش ها برای حسابدار چه شکلی باشد
def add_transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    context = {
        'form': form,
    }
    return render(request, 'finances/addTransactions.html', context)
#------------------------------------------------------------------------------------------------------
@login_required
def profile_edit_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    context = {'profile_form': form}
    return render(request, 'finances/profile_edit.html', context)