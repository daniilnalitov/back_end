"""
URL configuration for films project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/', include('filmsai_rest.urls'))
]

# дополнительные ендпоинты в режиме разработчика
if settings.DEBUG:
    # Создание представления для Swagger (OpenApi)
    schema_view = get_schema_view(
        openapi.Info(
            title='FilmsAi API',
            default_version='v1',
        ),
        public=True
    )
    # Добавление ендпоинтов для Swagger (OpenApi)
    urlpatterns += [
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
 # остальные ендпоинты (статические и пользовательские файлы)

    # добавление ендпоинтов со статическими файлами
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # добавление ендпоинтов с пользовательскими файлами
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)