from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

## Login View ##
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect('/') # Redirect to homepage
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form 
    }
    return render(request, "accounts/login.html", context)


## Logout View ##
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/') # Redirect to Login Page
    return render(request, "accounts/logout.html", {})


## Register View ## 
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)