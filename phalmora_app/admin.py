from django.contrib import admin
from .models import Contact, RecruiterContact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'subject', 'created_at')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',) 



@admin.register(RecruiterContact)
class RecruiterContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'subject', 'created_at')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',) 