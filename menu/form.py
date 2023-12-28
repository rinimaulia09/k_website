from django import forms

from .models import kategori

class FromBuku( forms.Form):
    kategori = forms.ModelChoiceField(queryset=kategori.objects.all())
    nama_pinjam = forms.CharField(max_length=100)
    judul_buku = forms.CharField(max_length=100)
    tgl_pinjam = forms.DateField()
    kembalian = forms.DateField() 
