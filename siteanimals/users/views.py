from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm,RegisterUserForm, ProfileUserForm,UserPasswordChangeForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm,PasswordChangeView
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProfileUser(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'header': "Профиль пользователя"
    }
    def get_success_url(self):
        return reverse_lazy('users:profile',args=[self.request.user.pk])
    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {
        'title' : "Изменение пароля",
        'header': "Изменение пароля"
    }
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