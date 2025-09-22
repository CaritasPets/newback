from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (
    RegisterView,
    ProfileView,
    DeleteView,
    LoginView,
)
from adocao.views import (
    PetAdocaoViewSet,
    PetPerdidoViewSet
)

router = DefaultRouter()

router.register(r"adocao", PetAdocaoViewSet)
router.register(r"perdidos", PetPerdidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    #users
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/profile/', ProfileView.as_view(), name="profile"),
    path('api/delete-user/', DeleteView.as_view(), name="delete-user"),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name="refresh-token"),
]
