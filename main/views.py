from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import InquiryForm

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def support_home(request):
    return render(request, 'support_home.html')

@login_required
def camera_integration(request):
    return render(request, 'camera_integration.html')

@login_required
def notifications(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notifications') 
    else:
        form = InquiryForm()
    
    return render(request, 'notifications.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})  # 경로가 'accounts/signup.html'로 수정


