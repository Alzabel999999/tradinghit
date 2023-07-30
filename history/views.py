from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
import json

# Create your views here.
class FrontendTemaplateView(View):
    def get(self, request):
        context = {
            'get_data': [1,2,3,4]
        }



        # Отправляем клиенту отрендеренный с контекстом шаблон
        return render(request, 'history/index.html', context)

    def post(self, request):
        # Собираем все параметры запроса в контекст
        context = {
        	'post_data': request.body,
          'get_data': json.dumps(request.GET) # Сериализуем в JSON
        }

        # Отправляем клиенту отрендеренный с контекстом шаблон
        return render(request, 'history/main.html', context)
