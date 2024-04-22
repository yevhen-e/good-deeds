from django.contrib import admin
from .models import Country, Location, State, City, Category, Image, Item


class CountryAdmin(admin.ModelAdmin):
    fields = ['name']

class StateAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

class CityAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

class LocationAdmin(admin.ModelAdmin):
    fields = ['country', 'state', 'city']
    list_display = ['country', 'state', 'city']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image_path']
    list_display = ['name', 'image_path']

class ImageAdmin(admin.ModelAdmin):
    fields = ['item', 'image_path']
    list_display = ['item', 'image_path']

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'description', 'author', 'location', 'pub_date']
    list_display = ['title', 'category', 'author', 'location', 'pub_date']
    inlines = [ImageInline]
    list_filter = ('author', 'location','pub_date')
    

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Item, ItemAdmin)