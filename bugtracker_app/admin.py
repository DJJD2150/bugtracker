from django.contrib import admin
from bugtracker_app.models import Ticket, CustomUserModel

# Register your models here.
admin.site.register(Ticket)
admin.site.register(CustomUserModel)