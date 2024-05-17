from django.contrib import admin
from .models import Slider, TeamMember, Service, ServiceImages, AboutInfo, ContactData, ProductImages, BlogCategory, Blog, BlogImages, Faq, Contacts, Product, Sign, Video

# Register your models here.


class BlogImagesInline(admin.TabularInline):
    model = BlogImages
    extra = 2


class ServiceImagesInline(admin.TabularInline):
    model = ServiceImages
    extra = 2


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImagesInline]
    prepopulated_fields = {'slug': ('title',)}


class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImagesInline]
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    prepopulated_fields = {'slug': ('name',)}


class ContactDataAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")


admin.site.register(Slider)
admin.site.register(TeamMember)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AboutInfo)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contacts)
admin.site.register(Video)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sign)
admin.site.register(Faq)
admin.site.register(ContactData)
