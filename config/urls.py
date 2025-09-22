from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from adocao.views import (
    PetAdocaoViewSet,
    PetPerdidoViewSet
)

router = DefaultRouter()

router.register(r"adocao", PetAdocaoViewSet)
router.register(r"perdidos", PetPerdidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
