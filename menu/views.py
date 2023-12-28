from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import kategori, Buku
from .form import FromBuku
from django.views.decorators.csrf import csrf_exempt


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
  data = Buku.objects.get(id=id)
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

@csrf_exempt
def list(request):
  submitted = False
  if request.method == "POST":
    form = FromBuku(request.POST)
    if form.is_valid():
      simpanData = Buku.objects.create(
          kategori = form.cleaned_data.get("kategori"),
          nama_pinjam = form.cleaned_data.get("nama_pinjam"),
          judul_buku = form.cleaned_data.get("judul_buku"),
          tgl_pinjam = form.cleaned_data.get("tgl_pinjam"),
          kembalian = form.cleaned_data.get("kembalian"), 
      )
      simpanData.save()
      return HttpResponseRedirect("/list?submitted=True")
  else:
    form = FromBuku
    if "submitted" in request.GET:
      submitted = True
  context = {
    "form": FromBuku,
  }
  template = loader.get_template('list.html')
  return HttpResponse(template.render(context, request))
