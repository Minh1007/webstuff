from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display.append("get_category_name")

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.short_description = "CATEGORY"

class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'rating', 'site_url', 'staff_comment']
    list_display.append("get_category_name")
    list_display.append("get_subcategory_name")

    def get_category_name(self, obj):
        return obj.category.name
    def get_subcategory_name(self, obj):
        return obj.subcategory.name

    get_category_name.short_description = "CATEGORY"
    get_subcategory_name.short_description = "SUB CATEGORY"

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Content, ContentAdmin)

