from django.shortcuts import render

def home():
    return render(request, 'user/home.html')