from django.contrib import admin
from .models import Sausage
# Register your models here.

class SausageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "current_price", "created"]
    
admin.site.register(Sausage, SausageAdmin)    