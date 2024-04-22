from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ['text', 'sender', 'recipient', 'pub_date', 'item']
    list_display = ['text','sender', 'recipient', 'pub_date', 'item']


admin.site.register(Message, MessageAdmin)