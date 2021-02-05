from django.contrib import admin

# Register your models here.
from .models import room, switchboard
admin.site.register(room)
admin.site.register(switchboard)