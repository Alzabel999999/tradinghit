from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include

urlpatterns = [
    path('v1/get_candles/', GetCandlesView.as_view()),
]
