from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    #search_fields = []

@admin.action(description='Убрать возможность торга')
def make_auction_as_false(self, reqquest, queryset):
    queryset.update(auction=False)

@admin.action(description='Добвавить возможность торга')
def make_auction_as_false(self, reqquest, queryset):
    queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
