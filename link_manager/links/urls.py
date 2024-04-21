from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from links.views import (LinkViewSet,
                         CollectionViewSet,
                         ChangePasswordView,
                         RegisterUser,
                         LoginAPIView,
                         PasswordResetView,
                         PasswordResetConfirmView
                         )

router = routers.DefaultRouter()
router.register(r'links', LinkViewSet, basename='links')
router.register(r'collections', CollectionViewSet, basename='collections')

schema_view = get_schema_view(
    openapi.Info(
        title="Link Manager API",
        default_version="v1",
        description="Документация для API по управлению ссылками и коллекциями",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


urlpatterns += router.urls
