from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import SignUpForm, ActivateForm
from users.models import OneTimeCode
from users.services import generate_random_string


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        new_user.save()
        code = generate_random_string()
        OneTimeCode.objects.create(code=code, user=new_user)
        print(code)
        send_mail(
            subject='Подтвердите ваш аккаунт!',
            message=f'{new_user.username}, для завершения регистрации введите код {code}, перейдя по '
                    f'<a href="http://127.0.0.1:8000/users/activate_account/">ссылке</a>!',
            from_email=None,
            recipient_list=[new_user.email],
        )
        return render(self.request, 'registration/activate_account.html', context={'form': ActivateForm})


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('adverts_list')


def activate_account(request):
    username = request.POST.get('username')
    code = request.POST.get('code')
    one_time_code = get_object_or_404(OneTimeCode, code=code, user__username=username)
    user = one_time_code.user
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('/adverts')


def logout_user(request):
    logout(request)
    return redirect('/adverts')
