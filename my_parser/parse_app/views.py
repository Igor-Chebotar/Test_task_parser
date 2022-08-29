from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .service import yandex_parse


class MainView(TemplateView):
    template_name = 'news.html'

    def get(self, request):
        data = yandex_parse()
        ctx = {'news': data}
        return render(request, self.template_name, ctx)


class NewsDataView(APIView):
    def get(self, request):
        data = yandex_parse()
        return Response(data)

