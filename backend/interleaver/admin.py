from django.contrib import admin
from .models import Interleaver

class InterleaverAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Interleaver, InterleaverAdmin)