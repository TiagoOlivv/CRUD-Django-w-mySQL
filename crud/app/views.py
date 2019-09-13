from django.shortcuts import render

def home(request):
    var = 'teste'
    return render(request, 'user/home.html', {'var' : var})