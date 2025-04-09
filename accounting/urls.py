from django.urls import path
from . import views


urlpatterns = [
    path('accounting/', views.add_payments, name='add_payments'),
    path('alladdpayments/', views.add_payments, name='all_add_payments'),
    path('allpayments/<int:student_id>/', views.payment_regi, name='payments'),
    path('viewpayments/', views.view_payments, name='view_payments'),
    path('changestatus/<int:student_status_id>/', views.change_status, name='change_status'),
]