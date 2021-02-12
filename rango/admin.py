from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class Page_Admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']


admin.site.register(Category)
admin.site.register(Page, Page_Admin)