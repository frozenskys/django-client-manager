from django.contrib import admin
from baclients.clients.models import Client, ClientNote
from baclients.clients.models import Access, AccessNote, Contact

class AccessNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'access', 'timestamp')
    search_fields = ('access__client',)
    list_filter = ('access',)
    
class AccessNoteInline(admin.StackedInline):
    model = AccessNote
    max_num = 2

class AccessAdmin(admin.ModelAdmin):
    list_display = ('client', 'access_type', 'url', 'username', 'password')
    search_fields = ('client__name', 'access_type')
    list_filter = ('client', 'access_type')
    inlines = [AccessNoteInline]
    
class AccessInline(admin.TabularInline):
    model = Access
    max_num = 5
    fields = ('access_type', 'url', 'username', 'password')
        
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'email', 'primary_phone')
    search_fields = ('client__name', 'name')
    list_filter = ('client',)
    
class ContactInline(admin.TabularInline):
    model = Contact
    max_num = 3

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_title')
    inlines = [ContactInline, AccessInline]
    
class ClientNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'timestamp')
    search_fields = ('client__name', 'title')
    list_filter = ('client',)
                    
admin.site.register(Access, AccessAdmin)
admin.site.register(AccessNote, AccessNoteAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientNote, ClientNoteAdmin)
admin.site.register(Contact, ContactAdmin)
