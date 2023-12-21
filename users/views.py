from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User
from users.tasks import send_reg_email, new_password, send_new_pass_email


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_reg_email(new_user)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    send_new_pass_email(request)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:HomeListView'))
