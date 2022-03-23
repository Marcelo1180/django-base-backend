from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from base.apps.account.views import view_status
# from django.conf.urls.static import static


urlpatterns = [
    path("", view_status),
    path("account/v1/", include("base.apps.account.urls")),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Show apidoc if DEBUG is activated
schema_view = get_schema_view(
    openapi.Info(
        title="Project Base v1",
        default_version="v1",
        description="Base Django",
        terms_of_service="https://raw.githubusercontent.com/Marcelo1180/django-base-backend/main/LICENSE",
        contact=openapi.Contact(email="arteagamarcelo@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
        re_path(
            r"^apidoc(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^apidoc/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
    # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

