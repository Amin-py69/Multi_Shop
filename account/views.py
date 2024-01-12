from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = authenticate(username=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_index')
            else:
                form.add_error('phone', 'your phone or password is wrong')
        else:
            form.add_error('phone', 'invalid your data')