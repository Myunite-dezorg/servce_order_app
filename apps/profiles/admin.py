from django.contrib import admin
from .models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'agent_id',
        'phone',
        'user_img',
        # 'barcode_preview'
    
   ]
    search_fields = ['user__email','agent_id',]