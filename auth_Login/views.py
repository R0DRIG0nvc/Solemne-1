from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def loginUser(request):
    template_name = '../Template/Login/login.html'
    data = {}

    logout(request)
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basket_matchList'))
            else:
                print("usuario o contraseña no validos")
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            print("Usuario incorrecto")
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )
    return render(request, template_name, data)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_Login_login'))
