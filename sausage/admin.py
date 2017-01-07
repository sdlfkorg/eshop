from django.contrib import admin
from .models import Sausage, Category, Tag
# Register your models here.

class SausageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "current_price", "created"]
    
admin.site.register(Sausage, SausageAdmin)    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass