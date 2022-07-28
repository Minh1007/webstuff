from django.contrib import admin
from .models import *
from django import forms

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display.append("get_category_name")

    def get_category_name(self, obj):
        return obj.category.name

    get_category_name.short_description = "CATEGORY"



class ContentForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)
    class Meta:
        fields = ('__all__')
        model = Content

class ContentAdmin(admin.ModelAdmin):
    form = ContentForm

    list_display = ['id', 'name', 'desc', 'rating', 'site_url', 'staff_comment']
    list_display.append("get_category_name")
    list_display.append("get_subcategory_name")
    list_display.append("get_stuff_name")
    change_form_template = 'admin/content_admin_form.html'

    def get_category_name(self, obj):
        return obj.category.name
    def get_subcategory_name(self, obj):
        return obj.subcategory.name
    def get_stuff_name(self, obj):
        return obj.admin.email

    get_category_name.short_description = "CATEGORY"
    get_subcategory_name.short_description = "SUB CATEGORY"
    get_stuff_name.short_description = "Stuff Email"

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(tbl_user)

