from django.contrib import admin
from .models import kategori, Produk

# Register your models here.
class ProdukKategori(admin.ModelAdmin):
    list_display = ("namaProduk", "harga")

admin.site.register(Produk, ProdukKategori)
admin.site.register(kategori)
