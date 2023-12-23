from django.http import HttpResponse
from django.template import loader
from .models import kategori, Produk

def members(request):
  data = kategori.objects.all()
  context = {
    "judul":"welcome",
    "sub_judul" :"website",
    "kategori" : data,
  }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, request))

def produk(request):
  data = Produk.objects.all().values()
  context = {
    "data" : data,
  }
  template = loader.get_template('produk.html')
  return HttpResponse(template.render(context, request))

def detail_produk(request, id):
  data = Produk.objects.get(id=id)
  template = loader.get_template('detail_produk.html')
  context = {
    'produk': data,
  }
  return HttpResponse(template.render(context, request))