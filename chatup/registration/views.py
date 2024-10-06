from django.shortcuts import render


def sign_in(request):
    return render(request, 'registration/html/sign_in.html')
