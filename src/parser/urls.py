from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TariffViewSet, MainAPIView

app_name = 'parser'

router = SimpleRouter()

router.register('', TariffViewSet)

urlpatterns = [path('', MainAPIView.as_view(), name='main'),
               path('get_tariffs/',
                    TariffViewSet.as_view({'get': 'get_tariffs'}),
                    name='get_tariffs'),
               path('parser/',
                    TariffViewSet.as_view({'get': 'parser'}),
                    name='parser'),
               ] + router.urls
