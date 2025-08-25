from django.contrib import admin
from .models import Property, Contact, Agent

admin.site.register(Agent)
# Customize admin site headers
admin.site.site_header = "RDH Admin"
admin.site.site_title = "RDH Admin Portal"
admin.site.index_title = "Welcome to RDH Accommodation Portal"

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'property_type', 'price', 'location', 'owner', 'email', 'phone', 'baths', 'created_at'
    )
    list_filter = ('property_type',)
    search_fields = ('title', 'location', 'description', 'owner', 'email', 'phone', 'baths')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'property_type', 'price', 'beds', 'baths', 'area', 'location',
                'description', 'image', 'owner', 'email', 'phone',
                'created_at', 'updated_at'
            )
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    def save_model(self, request, obj, form, change):
        if not change:  
            if not obj.user_id:  
                obj.user = request.user  
        super().save_model(request, obj, form, change)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
