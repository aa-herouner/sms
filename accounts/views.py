# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import UserLoginForm

# # Create your views here.
# def user_login(request):
#     forms = UserLoginForm()
#     if request.method == "POST":
#         forms = UserLoginForm(request.POST)
#         if forms.is_valid():
#             username = forms.cleaned_data["username"]
#             password = forms.cleaned_data["password"]

#             user = authenticate(username=username, password=password)

#             if user:
#                 login(request, user)
#                 return redirect("home")
#             else:
#                 messages.error(request, "Invalid User or Password")
#                 return redirect("login")

#     context = {
#         "forms": forms
#     }
#     return render(request, "accounts/login.html", context)

# def user_logout(request):
#     logout(request)
#     return redirect("login")



# def my_view(request):
#     accounts = User.objects.all()
#     return render(request, 'accounts/breadcrumb.html', {'accounts': accounts})

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomLoginForm

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page after login
        else:
            form = CustomLoginForm()
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

