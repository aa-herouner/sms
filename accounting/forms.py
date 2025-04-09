from django import forms
from .models import PaymentsInformation
from django.core.exceptions import ValidationError



# class StudentsPayment(forms.ModelForm):
#     class Meta:
#         model = PaymentsInformation
#         fields = "__all__"

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'readonly' : True}),
#             'class_type': forms.Select(attrs={'class': 'form-control', 'readonly' : True}),
#             'month': forms.Select(attrs={'class': 'form-control'}),
#             'session': forms.Select(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

    # def duplicate_entry(self):
    #     name = self.cleaned_data.get('name')
    #     month = self.cleaned_data.get('month')
    #     if PaymentsInformation.objects.filter(name=name, month=month).exists():
    #         raise forms.ValidationError(f"{name} + 'payment of' + {month} already exists")
        
class StudentsPayment(forms.ModelForm):
    class Meta:
        model = PaymentsInformation
        fields = ['name', 'class_type', 'month', 'session', 'status']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'readonly' : True}),
            'class_type': forms.Select(attrs={'class': 'form-control', 'readonly' : True}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    # def clean_month(self):
    #     # cleaned_data = super().clean()
    #     month = self.cleaned_data.get('month')
    #     name = self.cleaned_data.get('name')
    #     error = f"Payment for {name} in {month} + already exists."

     
    #     if PaymentsInformation.objects.filter(name=name, month=month).exists():
    #         raise forms.ValidationError(error) 
        
        # return cleaned_data 

