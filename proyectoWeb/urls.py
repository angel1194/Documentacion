"""proyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from AppEquipos import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.generales,name="home"),
    path('detalles/<int:id>',views.detalles,name="detalles"),
    path('acer/',views.acer,name="acer"),
    path('apple/',views.apple,name="apple"),
    path('asus/',views.asus,name="asus"),
    path('compaq/',views.compaq,name="compaq"),
    path('dell/',views.dell,name="dell"),
    path('gateway/',views.gateway,name="gateway"),
    path('hp/',views.hp,name="hp"),
    path('huawei/',views.huawei,name="huawei"),
    path('lenovo/',views.lenovo,name="lenovo"),
    path('msi/',views.msi,name="msi"),
    path('samsung/',views.samsung,name="samsung"),
    path('sony/',views.sony,name="sony"),
    path('toshiba/',views.toshiba,name="toshiba"),
    path('documentacion/',views.documentacion,name="documentacion"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
