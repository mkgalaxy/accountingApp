from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction

def welcome_view(request):
    return render(request, 'finances/welcome.html')

def login_view(request):
    return render(request, 'finances/login.html')

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
