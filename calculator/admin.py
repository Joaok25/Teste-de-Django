from django.contrib import admin
from .models import Operation

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'op_type', 'expression', 'result', 'created_at')
    list_filter = ('op_type', 'created_at')
    search_fields = ('expression', 'user__username')
