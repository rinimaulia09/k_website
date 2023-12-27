from django.db import models
from django.contrib import admin

# Create your models here.
class kategori (models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama}"

# admin.site.register(kategori)

class Buku (models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    nama_pinjam = models.CharField(max_length=100)
    judul_buku = models.CharField(max_length=100)
    tgl_pinjam = models.DateField()
    kembalian = models.DateField() 

    def __str__(self):
        return f"{self.nama_pinjam} {self.judul_buku} {self.tgl_pinjam} {self.kembalian} "

# admin.site.register(Buku)  