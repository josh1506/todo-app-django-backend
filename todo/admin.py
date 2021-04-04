from django.contrib import admin
from .models import Todo, CheckList


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'memo', 'cover', 'status')
    list_filter = ('user', 'memo', 'status')
    search_fields = ('user', 'memo', 'status')
    exclude = ('date_created',)


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ('todo', 'text', 'status')
    list_filter = ('todo', 'text', 'status')
    search_fields = ('todo', 'text', 'status')
    exclude = ('date_created',)
