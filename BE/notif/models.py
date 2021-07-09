from django.shortcuts import reverse
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class Keyword(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Me(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.ManyToManyField(Keyword, blank=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_me(sender, instance, created, **kwargs):
    if created:
        print(instance)


@receiver(post_save, sender=Item)
def create_item(sender, instance, created, **kwargs):
    if created:
        print("Item Created!")


@receiver(post_save, sender=Item)
def notify_user(sender, instance, **kwargs):
    item_kw = instance.category

    # Item Model
    mes = Me.objects.all()

    for me in mes:
        my_interest = me.interest.all()

        if item_kw in my_interest:
            from notif.views import notify_me
            notify_me(item_kw=item_kw)
            print(f"Yess, it's in there! Look, {item_kw}")
        else:
            print("Oof, it's not there. Maybe next time?")
