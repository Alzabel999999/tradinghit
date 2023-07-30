from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', FrontendTemaplateView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
