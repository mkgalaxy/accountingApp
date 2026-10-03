from django.db import models
from django.contrib.auth.models import User
#--------------------------------------------------------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    storeName = models.CharField(max_length=200, verbose_name="نام فروشگاه / شرکت")
    phoneNumber = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تماس")
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='تصویر پروفایل')
    def __str__(self):
        return f"{self.storeName} ({self.user.username})"
#--------------------------------------------------------------------------------------------------
class Transaction(models.Model):
    TT = [ # نوع تراکنش ها
        ('income', 'درآمد / فروش'),
        ('expense', 'هزینه / خرید'),
    ]
    PM = [ # نحوه پرداخت
        ('cash', 'نقدی'),
        ('pos', 'کارتخوان'),
        ('credit', 'نسیه / حساب دفتری'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="حسابدار / کاربر")
    title = models.CharField(max_length=255, verbose_name="شرح تراکنش")
    amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="مبلغ")
    transactionType = models.CharField(max_length=10, choices=TT, verbose_name="نوع تراکنش")
    paymentMethod = models.CharField(max_length=10, choices=PM, default='pos', verbose_name="نوع پرداخت")
    customerName = models.CharField(max_length=150, blank=True, null=True, verbose_name="نام مشتری")
    date = models.DateField(verbose_name="تاریخ تراکنش")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت در سیستم")
    def __str__(self):
        return f"{self.title} - {self.amount} تومان ({['نقدی', 'کارتخوان', 'نسیه'][['cash', 'pos', 'credit'].index(self.paymentMethod)]})"