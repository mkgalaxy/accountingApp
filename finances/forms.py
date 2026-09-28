from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transactionType', 'paymentMethod', 'customerName', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'loginInput', 'placeholder': 'شرح تراکنش'}),
            'amount': forms.NumberInput(attrs={'class': 'loginInput', 'placeholder': 'مبلغ(تومان)'}),
            'transactionType': forms.Select(attrs={'class': 'loginInput'}),
            'paymentMethod': forms.Select(attrs={'class': 'loginInput'}),
            'customerName': forms.TextInput(attrs={'class': 'loginInput', 'placeholder': 'نام مشتری'}),
            'date': forms.DateInput(attrs={'class': 'loginInput', 'type': 'date'}),
        }
