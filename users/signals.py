from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, nickname=instance.username)
        print(f"Profile of user {instance.username} has been created")


@receiver(post_save, sender=UserProfile)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Добро пожаловать!",
            f"Благодарим за регистрацию, дорогой {instance.nickname}",
            "example@localhost",
            [instance.user.email],
            fail_silently=False,
        )
