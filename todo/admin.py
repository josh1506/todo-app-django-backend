from django.contrib import admin
from .models import Todo, CheckList


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'memo', 'status')
    list_filter = ('user', 'status')
    search_fields = ('user', 'memo', 'status')
    exclude = ('date_created',)


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo', 'text', 'status')
    list_filter = ('todo', 'status')
    search_fields = ('todo', 'text', 'status')
    exclude = ('date_created',)
