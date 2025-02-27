from django.urls import path
from .views import (
    CreateClickTransactionView,
    ClickTransactionTestView,
    ClickMerchantServiceView,
)



urlpatterns = [
    path("", CreateClickTransactionView.as_view()),
    path("process/click/transaction/", ClickTransactionTestView.as_view()),
    path("process/click/service/<service_type>", ClickMerchantServiceView.as_view()),
]
