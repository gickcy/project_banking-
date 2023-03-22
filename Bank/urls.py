from .views import UserRegistrationView, LogoutView, UserLoginView
from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView
app_name='Bank'

urlpatterns = [
    path("login/", UserLoginView.as_view(),name="user_login"),
    path("logout/", LogoutView.as_view(),name="user_logout"),
    path("register/", UserRegistrationView.as_view(),name="user_registration"),
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]
