import django_filters
from .models import *
from django import forms

class StatusFilters(django_filters.FilterSet):
    class Meta:
        model = PaymentsInformation
        fields = '__all__'
        exclude = ['name', 'class_type', 'month', 'session']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }