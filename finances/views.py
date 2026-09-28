from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
def welcome_view(request):
    return render(request, 'finances/welcome.html')
#------------------------------------------------------------------------------------------------------
def login_view(request):
    return render(request, 'finances/login.html')
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
