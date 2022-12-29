from django.contrib import admin

from tree_menu.models import TreeMenu

class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'named_url', 'parent_id')
    list_display_links = ('name',)
    prepopulated_fields = {"named_url": ("url",)}


admin.site.register(TreeMenu, TreeMenuAdmin)
