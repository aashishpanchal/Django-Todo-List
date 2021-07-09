from django.contrib import admin
from .models import TODOModel

# Register your models here.
@admin.register(TODOModel)
class TODOModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Title', 'Description', 'Important', 'DateTime']