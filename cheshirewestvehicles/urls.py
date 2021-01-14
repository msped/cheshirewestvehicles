"""cheshirewestvehicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views import static
from home.views import Home
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('buy/', include('sales.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),
    path('business-admin/', include('business_admin.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]

handler400 = 'error_handling.views.handler400'
handler403 = 'error_handling.views.handler403'
handler404 = 'error_handling.views.handler404'
handler500 = 'error_handling.views.handler500'
