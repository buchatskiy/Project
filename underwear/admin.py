from django.contrib import admin
from underwear.models import Series, Color, Underwear, Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_number', 'first_name', 'totalprice', 'phone_number', 'city', 'post_office', 'divisions', 'date', 'comment', 'underwear',)
    list_filter = ('date',)
    ordering = ('-date',)

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('name',)

class UnderwearAdmin(admin.ModelAdmin):
    list_display = ('idu', 'availableM', 'availableL', 'availableXL', 'series', 'color')
    search_fields = ['idu']
    ordering = ('idu',)

admin.site.register(Series, SeriesAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Underwear, UnderwearAdmin)
admin.site.register(Color)