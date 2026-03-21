from django.contrib import admin
from .models import Contact, Project



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'created_at')
	search_fields = ('name', 'phone', 'message')
	list_filter = ('created_at',)
	readonly_fields = ('created_at',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack')
