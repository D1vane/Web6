from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm,RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация",
                     'header': "Авторизация"}

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {
        'title' : "Регистрация",
        'header' : "Регистрация"
    }
    success_url = reverse_lazy('users:login')
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
        return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponse(reverse('users:login'))

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
        else:
            form = RegisterUserForm()
            return render(request, 'users/registration.html', {'form': form})