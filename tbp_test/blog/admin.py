from django.contrib import admin
from blog.models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'upa', 'pda', 'created_on']

admin.site.register(Url, UrlAdmin)
