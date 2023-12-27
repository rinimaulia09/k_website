from django.http import HttpResponse
from django.template import loader
from .models import kategori, Buku

def members(request):
  data = kategori.objects.all()
  context = {
    "judul":"",
    "sub_judul" :"",
    "kategori" : data,
  }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, request))

def book(request):
  data = Buku.objects.all().values()
  context = {
    "data" : data,
  }
  template = loader.get_template('book.html')
  return HttpResponse(template.render(context, request))

def detail_buku(request, id):
  data = Produk.objects.get(id=id)
  template = loader.get_template('detail_buku.html')
  context = {
    'buku': data,
  }
  return HttpResponse(template.render(context, request))

def dt(request):
  context = {
  }
  template = loader.get_template('dt.html')
  return HttpResponse(template.render(context, request))

def list(request):
  context = {
  }
  template = loader.get_template('list.html')
  return HttpResponse(template.render(context, request))
