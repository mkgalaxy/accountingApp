from django.contrib import admin
from .models import UserProfile, Transaction
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'storeName', 'phoneNumber')
    search_fields = ('user__username', 'storeName')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'transactionType', 'paymentMethod', 'customerName', 'date')
    list_filter = ('transactionType', 'paymentMethod', 'date', 'user')
    search_fields = ('title', 'user__username', 'customerName')