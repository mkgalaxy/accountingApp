from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard_view , name='dashboard'),
    path('transactions/add', views.add_transaction_view , name='add_transaction'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]