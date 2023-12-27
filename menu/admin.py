from django.contrib import admin
from .models import kategori, Buku

# Register your models here.
class Kategori(admin.ModelAdmin):
    list_display = ("nama_pinjam", "judul_buku", "tgl_pinjam", "kembalian")

admin.site.register(Buku)
admin.site.register(kategori)