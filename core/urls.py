


from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path
from django.conf import settings

from django.conf.urls.static import static

from django.shortcuts import render
from core import views as core_views

# Add this import for browser reload
import django_browser_reload

schema_view = get_schema_view(
    openapi.Info(
        title="eventspace-api",
        default_version='v1',
        description="A REST API for an event-space system.",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.authentication.urls')),
    path('api/spaces/', include('apps.spaces.urls')),
    path('api/bookings/', include('apps.bookings.urls')),
    path('events/', core_views.events_view, name='events-page'),
    path('register/', core_views.register_view, name='register-page'),
    path('login/', core_views.login_view, name='login-page'),
    path('logout/', core_views.logout_view, name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),

    # Direct template views with context
    path('spaces/', core_views.spaces_view, name='spaces-page'),
    path('spaces/view/', core_views.space_detail_view, name='space-detail'),
    path('spaces/view/', core_views.spaces_view, name='spaces-view'),
    path('bookings/', core_views.bookings_view, name='bookings-page'),
    path('bookings/view/', core_views.bookings_view, name='bookings-view'),
    path('home/', core_views.home_view, name='home-page'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
