from celery import shared_task
from django.core.mail import send_mail
from root import settings


# @shared_task
# def send_email_customer(message):
#     # print('Sending message')
#     # msg = f'''
#     # {name}, {email}, {phone}, {message}
#     # '''
#     # print(msg)
#     # send_mail(
#     #     subject="Qalampir.uz",
#     #     message=message,
#     #     from_email=settings.EMAIL_HOST_USER,
#     #     recipient_list=['diordev@icloud.com'],
#     #     fail_silently=False,
#     # )

@shared_task
def send_message_email(message, email):
    send_mail(
        subject="We are happy to cooperate with you!",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False, )