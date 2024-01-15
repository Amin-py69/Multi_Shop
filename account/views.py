from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, RegisterForm, OtpCheckCodeForm
from django.contrib.auth import authenticate, login, logout
from .models import RegisterOtp, User
import ghasedakpack
from random import randint

SMS = ghasedakpack.Ghasedak("1205cbf0a351107afb5c4abec80f0705840b4f0fe6b1b4f123b2e5d2ff526f24")


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
            form.add_error('phone', 'invalid your data your should registering')

        return render(request, 'account/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            random_code = randint(1000, 9999)
            SMS.verification({'receptor': phone, 'type': '1', 'template': 'randcode', 'param1': random_code})
            RegisterOtp.objects.create(phone=phone, code=random_code)
            print(random_code)
            return redirect(reverse('account:otp_code') + f'?phone={phone}')
        else:
            form.add_error('phone', 'your phone or password is wrong')

        return render(request, 'account/register.html', {'form': form})


class OtpCheckCodeView(View):
    def get(self, request):
        form = OtpCheckCodeForm()
        return render(request, 'account/otp_code.html', {'form': form})

    def post(self, request):
        phone = request.GET.get('phone')
        form = OtpCheckCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if RegisterOtp.objects.filter(code=code, phone=phone).exists():
                user = User.objects.create_user(phone=phone)
                login(request, user)
                return redirect('home:home_index')
        else:
            form.add_error('phone', 'your phone or password is wrong')

        return render(request, 'account/otp_code.html', {'form': form})
