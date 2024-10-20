from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, update_last_login
from .models import Perfil


@receiver(post_save, sender=User)
def registrar_login(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Perfil.objects.get_or_create(user=instance)
        instance.is_staff = True
        instance.is_superuser = True
        instance.save()

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        if not Perfil.objects.filter(user=instance).exists():
            Perfil.objects.create(user=instance)