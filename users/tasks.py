from random import randint

from django.conf import settings
from django.core.mail import send_mail

new_password = ''.join([str(randint(0, 9)) for _ in range(12)])


def send_reg_email(new_user):
    send_mail(
        subject='Поздравляем с регистрацией !',
        message=f'Для завершения регистрации, перейдите по ссылке '
                f'http://127.0.0.1:8000/users/verifying?code='
                f'{new_user.verified_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[new_user.email]
    )


def send_new_pass_email(request):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
