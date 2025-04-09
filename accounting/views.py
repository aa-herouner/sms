from django.shortcuts import render, get_object_or_404, redirect
from  students.models import StudentInfo
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import StudentsPayment
from .models import PaymentsInformation, PaymentStatus
from students.forms import CreateStudent
from .filters import StatusFilters
# Create your views here.

# def index(request):
#     return render(request, 'accounting/add_payments.html')

def add_payments(request):
    students = StudentInfo.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        "students": paged_students
    }
    return render(request, "accounting/add_payments.html", context)

# def payment_regi(request, student_id):
#     student = get_object_or_404(StudentInfo, id=student_id)

#     if request.method == 'POST':
#         payment_form = StudentsPayment(request.POST) 
#         if payment_form.is_valid():
#             payment = payment_form.save(commit=False)
#             payment.student = student 
#             payment.save()
#             return redirect('add_payments')
#         elif PaymentsInformation.objects.filter(name=payment_form.name, month=payment_form.month).exists():
#                 messages.error(request, 'The input already exists')     
#     else:
#         payment_form = StudentsPayment(initial={
#             'name': student.name,
#             'class_type': student.class_type, 
#         })

#     context = {
#         'payment_form': payment_form,
#         'student': student,
#     }
#     return render(request, 'accounting/payments.html', context)

def payment_regi(request, student_id):
    student = get_object_or_404(StudentInfo, id=student_id)

    if request.method == 'POST':
        payment_form = StudentsPayment(request.POST)
        if payment_form.is_valid():
            # Check if the payment already exists for the same name and month
            name = payment_form.cleaned_data['name']
            month = payment_form.cleaned_data['month']
            if PaymentsInformation.objects.filter(name=name, month=month).exists():
                messages.error(request, f'Payment for {payment_form.cleaned_data['name']}  already exists in {payment_form.cleaned_data['month']}.')
            else:
                payment = payment_form.save(commit=False)
                payment.student = student
                payment.save()
                messages.success(request, 'Payment added successfully.')
                return redirect('add_payments')
        else:
            messages.error(request, 'Form submission error. Please check your input.')
    else:
        payment_form = StudentsPayment(initial={
            'name': student.name,
            'class_type': student.class_type,
        })

    context = {
        'payment_form': payment_form,
        'student': student,
    }
    return render(request, 'accounting/payments.html', context)

def change_status(request, student_status_id):
    payment = PaymentsInformation.objects.get(id=student_status_id)
    paid_status = PaymentStatus.objects.get(status_name = 'Paid')

    if payment.status.status_name == 'Unpaid':
        payment.status = paid_status
        payment.save()
    return redirect('view_payments')


# def change_status(request, student_status_id):
#     status_id = get_object_or_404(PaymentsInformation, id=student_status_id)
#     edit_status = StudentsPayment(instance=status_id)

#     if edit_status.status == 'Unpaid':
#         st
#         # edit_status = StudentsPayment(request.POST, request.FILES or None, instance=status_id)

#         if edit_status.is_valid():
#             edit_status.save()
#             messages.success(request, "Edit Student Info Successfully!")
#             return redirect("student_list")

#     context = {
#         "edit_status": edit_status
#     }
#     return render(request, 'accounting/edit_payments.html', context)       


# def validation_message(request):
#     name = StudentsPayment('name')
#     month = StudentsPayment('month')

#     if request.method == 'POST':
#         if PaymentsInformation.objects.filter(name=name, month=month).exists():
#             messages.error(request, f"Payment for {name} in {month} + already exists.")

#     context = {
#         'name' : name,
#         'month' : month
#     }
#     return render(request, 'accounting/payments.html', context)

def view_payments(request):
    pay = PaymentsInformation.objects.all()
    
    myFilters = StatusFilters(request.GET, queryset=pay)
    filtered = myFilters.qs

    # paginator = Paginator(pay, 5)
    filtered_paginator = Paginator(filtered, 5)
    page = request.GET.get('page')
    paged_students = filtered_paginator.get_page(page)
    
    
    context = {
        'accounting' : paged_students,
        'myFilters' : myFilters
    }
    return render(request, "accounting/view_payments.html", context)

# def accounting_list(request):
#     # Fetch data from the Accounting model
#     accounting_data = PaymentsInformation.objects.all()  # Or add any filter if necessary
#     return render(request, 'accounting/view_payments.html', {'accounting': accounting_data})

# views.py




