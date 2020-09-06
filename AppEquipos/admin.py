from django.contrib import admin
from .models import Post,PostMarcas,Images
# Register your models here.


class AdminImages(admin.StackedInline):
    model = Images

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ("marca", "modelo","imagePortada")
    inlines = [AdminImages]
    class Meta:
       model = Post

class Marcas(admin.ModelAdmin):
    list_display = ("title",)
class AdImages(admin.ModelAdmin):
    list_display=("images",)

admin.site.register(Images,AdImages)
admin.site.register(PostMarcas,Marcas)
