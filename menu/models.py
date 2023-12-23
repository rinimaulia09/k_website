from django.db import models
from django.contrib import admin

# Create your models here.
class kategori (models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama}"

# admin.site.register(kategori)

class Produk (models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    namaProduk = models.CharField(max_length=100)
    harga = models.CharField(max_length=20)    

    def __str__(self):
        return f"{self.namaProduk} {self.harga}"

# admin.site.register(Produk)  