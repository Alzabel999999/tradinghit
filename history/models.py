from django.db import models

# Create your models here.
class TradingPair(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Торговая пара'
        verbose_name_plural = 'Торговые пары'

    def __str__(self):
        return self.name

class TimeFrame(models.Model):
    value = models.CharField(verbose_name='Значение', max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    def __str__(self):
        return self.value

class Candle(models.Model):
    timeframe = models.ForeignKey(TimeFrame, related_name='candle_timeframe', verbose_name='Таймфрейм', on_delete=models.CASCADE)
    trading_pair = models.ForeignKey(TradingPair, related_name='candle_trading_pair', verbose_name='Торговая пара', on_delete=models.CASCADE)
    time = models.DateTimeField('Время', null=True)
    utc = models.BigIntegerField('UTC', null=True)
    open = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Цена открытия', blank=True, null=True)
    high = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Цена высшая', blank=True, null=True)
    low = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Цена низшая', blank=True, null=True)
    close = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Цена закрытия', blank=True, null=True)
    volume = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='Обьемы торгов', blank=True, null=True)

    class Meta:
        verbose_name = 'Свеча'
        verbose_name_plural = 'Свечи'

    def __str__(self):
        return '{0} {1}'.format(self.trading_pair, self.timeframe)
