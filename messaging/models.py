from django.db import models
from django.conf import settings
from catalog.models import Item


class Message(models.Model):
    text = models.TextField(verbose_name='Message text')
    pub_date = models.DateField(verbose_name='Publication date')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='Sender', blank=True, default=None)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', verbose_name='Recipient', default=None, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)


