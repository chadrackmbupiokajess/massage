from django.contrib import admin
from .models import Service, ContactMessage, CarouselSlide, HomePageContent, Testimonial, AboutPageContent, Commitment, ContactPageContent

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'subtitle')

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    # To make sure only one object can be created
    def has_add_permission(self, request):
        return self.model.objects.count() == 0

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'is_visible', 'order')
    list_editable = ('is_visible', 'order')
    search_fields = ('author', 'quote')
    list_filter = ('is_visible',)

@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.count() == 0

@admin.register(Commitment)
class CommitmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(ContactPageContent)
class ContactPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.count() == 0
