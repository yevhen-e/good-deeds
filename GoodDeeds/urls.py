"""
URL configuration for GoodDeeds project.

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
from django.http import HttpResponse
from django.urls import path, include

from GoodDeeds.views import HomeView
from catalog.views import CatalogListView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('catalog/', include('catalog.urls')),
    path('', HomeView.as_view(template_name='home_view.html'), name='home_view'),
    path('<int:category_id>/', CatalogListView.as_view(template_name='items_list.html'), name='items_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)