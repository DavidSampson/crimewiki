from django.contrib import admin

from pages.models import Page, Entry, File, FileCollection, FileCategory, Location, WebResource

admin.site.register(Page)
admin.site.register(Entry)
admin.site.register(File)
admin.site.register(FileCollection)
admin.site.register(FileCategory)
admin.site.register(Location)
admin.site.register(WebResource)
