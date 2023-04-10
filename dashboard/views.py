from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from dashboard.forms import RegForm
 
# Views
def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, first_name = first_name, last_name = last_name, email = email, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = RegForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def repex(request):
    return render(request, 'repex/dashboard.html', {})