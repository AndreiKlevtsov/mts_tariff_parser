import logging

from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.main import get_source_code, tariff_parser
from .forms import TariffFilterForm
from .models import Tariff
from .serializers import TariffSerializer

logger = logging.getLogger(__name__)


class TariffViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    - `queryset` представляет набор объектов ингредиентов,
        к которым необходимо получить доступ.
    - `filter_backends`: Настроенный серверный модуль фильтра
        для фильтрации ингредиентов по названию.
    - `search_fields`: Поле `name' используется для поиска названия
        начинающегося с указанного значения.
    """
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parser/index.html'

    @action(detail=False, methods=('get',))
    def parser(self, request):
        tariff_cards = get_source_code()
        data = tariff_parser(tariff_cards)
        batch = [
            Tariff(name=row['name'],
                   description=row['description'],
                   features=row['features'],
                   benefits=row['benefits'],
                   main_price=row['main_price'],
                   sale_price=row['sale_price'],
                   price_annotation=row['price_annotation'],
                   badge_text=row['badge_text'],
                   ) for row
            in data
        ]
        names = [tariff_data['name'] for tariff_data in data]
        Tariff.objects.exclude(name__in=names).delete()
        Tariff.objects.bulk_create(
            batch, update_conflicts=True,
            unique_fields=['name'],
            update_fields=[
                'description',
                'features',
                'benefits',
                'main_price',
                'sale_price',
                'price_annotation',
                'badge_text'
            ]
        )
        logger.info(Tariff.objects.count())
        return redirect('/get_tariffs/')

    @action(detail=False, methods=['get'])
    def get_tariffs(self, request):
        queryset = Tariff.objects.all()
        form = TariffFilterForm(data=request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if data['is_gb']:
                queryset = queryset.filter(features__contains='ГБ')
            if data['is_tv']:
                queryset = queryset.filter(features__contains='ТВ')
            if data['is_min']:
                queryset = queryset.filter(features__contains='минут')

        context = {'page_obj': queryset, 'form': form}
        return render(request, 'parser/index.html', context)


class MainAPIView(APIView):
    """Отображает главную страницу"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parser/main.html'

    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)
