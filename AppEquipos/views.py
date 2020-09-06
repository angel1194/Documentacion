from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post,PostMarcas,Images
# Create your views here.
from django.forms import modelformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db.models import Q

def generales(request):
    query = request.GET.get('q')
    if query:
        post= Post.objects.filter(modelo__icontains = query)
    else:
        post= Post.objects.all()
    return render(request,"index.html",{'post':post,"query":query})

def acer(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="ACER")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/acer.html",{"post":post,"error":error})
def apple(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="APPLE")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/apple.html",{"post":post,"error":error})
def asus(request):
    error=None
    post=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="ASUS")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/asus.html",{"post":post,"error":error})
def compaq(request):
    error=None
    post = Post.objects.filter(
    marca=PostMarcas.objects.get(title="COMPAQ")
    )
    return render(request,"marcas/compaq.html",{"post":post})
def dell(request):
    error=None
    post=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="DELL")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/dell.html",{"post":post,"error":error})
def gateway(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="GATEWAY")
        )
    except ObjectDoesNotExist as e:
        error=e

    return render(request,"marcas/gateway.html",{"post":post,"error":error})
def hp(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="HP")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/hp.html",{"post":post,"error":error})
def huawei(request):
    error=None
    post=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="HUAWEI")
        )
    except ObjectDoesNotExist as e:
        error=e

    return render(request,"marcas/huawei.html",{"post":post,"error":error})
def lenovo(request):
    error=None
    post=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="LENOVO")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/lenovo.html",{"post":post,"error":error})
def msi(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="MSI")
        )
    except ObjectDoesNotExist as e:
        error=e

    return render(request,"marcas/msi.html",{"post":post,"error":error})
def samsung(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="SAMSUNG")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/samsung.html",{"post":post,"error":error})
def sony(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="SONY")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/sony.html",{"post":post,"error":error})
def toshiba(request):
    post=None
    error=None
    try:
        post = Post.objects.filter(
        marca=PostMarcas.objects.get(title="TOSHIBA")
        )
    except ObjectDoesNotExist as e:
        error=e
    return render(request,"marcas/toshiba.html",{"post":post,"error":error})

def detalles(request,id):
    detail= Post.objects.get(id=id)
    return render(request,"detalles.html",{'detail':detail})

def documentacion(request):
    return render(request,"blog/documentacion.html")
