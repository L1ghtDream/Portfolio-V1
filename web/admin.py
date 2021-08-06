from django.contrib import admin

from web.models import *


class EntryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


class SubEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "entry")


admin.site.register(Entry, EntryAdmin)
admin.site.register(SubEntry, SubEntryAdmin)
