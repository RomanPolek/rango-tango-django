from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
class Page_Admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, Page_Admin)
admin.site.register(UserProfile)