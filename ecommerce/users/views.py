from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form_signup = SignUpForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            username = form_signup.cleaned_data.get('username')
            raw_password = form_signup.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        
        form_signup = SignUpForm()
    return render(request, 'signup.html', {'form_signup': form_signup})