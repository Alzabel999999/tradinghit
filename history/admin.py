from django.contrib import admin, messages
from .models import TradingPair, TimeFrame, Candle
# Register your models here.

@admin.register(TradingPair)
class TradingPairAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ('name', )
    readonly_fields = []

@admin.register(TimeFrame)
class TimeFrameAdmin(admin.ModelAdmin):
    list_display = ['value',]
    list_display_links = ('value', )
    readonly_fields = []

@admin.register(Candle)
class TimeFrameAdmin(admin.ModelAdmin):
    list_display = ['trading_pair','timeframe', 'time', 'open', 'high', 'low', 'close', 'volume']
    list_display_links = ('trading_pair', )
    readonly_fields = []
    search_fields = ['trading_pair', 'timeframe']
    list_filter = ['trading_pair', 'timeframe']
