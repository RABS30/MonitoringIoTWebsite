from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import authUser

class CustomUserAdmin(UserAdmin):
    model           = authUser
    
    # daftar data user yang akan ditampilkan di dashboard
    list_display    = ('email', 'username', 'is_staff', 'is_active')
    # daftar filter yang tersedia
    list_filter     = ('is_staff', 'is_active')
    # urutan berdasarkan email
    ordering        = ('email', )
    # search hanya bisa relevan dengan email dan username
    search_fields   = ('email', 'username')
    
    # fieldsets saat mengedit user 
    fieldsets       = (
        (None, {'fields' : ('email', 'username', 'password')}),
        ('Personal info', {'fields' : ('first_name', 'last_name')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields' : ('last_login', 'date_joined')})
    )
    
    # fieldsets saat membuat user baru
    add_fieldsets = (
        (None, {
            'classes'   : ('Wide', ),
            'fields'    : ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    
admin.site.register(authUser, CustomUserAdmin)