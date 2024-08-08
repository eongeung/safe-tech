
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 폼이 유효하면
            user = form.save()  # 새로운 사용자 저장
            login(request, user)  # 자동 로그인
            return redirect('home')  # 메인 페이지로 리다이렉트
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})



