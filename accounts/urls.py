# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('accounts/', views.my_view, name='my_views'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
