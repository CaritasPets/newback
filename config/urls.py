from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenRefreshView

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from users.views import (
    RegisterView,
    ProfileView,
    DeleteView,
    LoginView,
    UpdateProfileView,
    ListCommonUserViewSet,
    ListOrganizationViewSet,
)
from adocao.views import PetAdocaoViewSet, PetPerdidoViewSet, FavoritoViewSet

router = DefaultRouter()

router.register(r"adocao", PetAdocaoViewSet)
router.register(r"perdidos", PetPerdidoViewSet)
router.register(r"organizations", ListOrganizationViewSet)
router.register(r"users", ListCommonUserViewSet)

favorito_view = FavoritoViewSet.as_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # favoritos
    path(
        "api/favoritos/adocao/<int:pk>/toggle/",
        favorito_view({"post": "toggle_adocao"}),
        name="favorito-adocao-toggle",
    ),
    path(
        "api/favoritos/perdidos/<int:pk>/toggle/",
        favorito_view({"post": "toggle_perdido"}),
        name="favorito-perdido-toggle",
    ),
    path(
        "api/favoritos/adocao/",
        favorito_view({"get": "list_adocao"}),
        name="favoritos-adocao",
    ),
    path(
        "api/favoritos/perdidos/",
        favorito_view({"get": "list_perdido"}),
        name="favoritos-perdidos",
    ),

    # users
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/profile/", ProfileView.as_view(), name="profile"),
    path("api/update/", UpdateProfileView.as_view(), name="update-profile"),
    path("api/delete-user/", DeleteView.as_view(), name="delete-user"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="refresh-token"),

    # tests
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
