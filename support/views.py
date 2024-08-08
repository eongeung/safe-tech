from django.shortcuts import render

def support_home(request):
    return render(request, 'support/support_home.html')
