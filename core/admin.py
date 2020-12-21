from django.contrib import admin
from .models import UsersIds	
from .models import SteamId


# Register your models here.
admin.site.register(UsersIds)
admin.site.register(SteamId)