from django.shortcuts import render
from mywatchlist.models import MyFilm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    my_watch_list = MyFilm.objects.all()
    context = {
        'watch_list' : my_watch_list,
        'nama' : 'Alifiaa',
        'NPM' : '2106634723'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    my_watch_list = MyFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", my_watch_list), content_type="application/xml")

def show_json(request):
    my_watch_list = MyFilm.objects.all()
    return HttpResponse(serializers.serialize("json", my_watch_list), content_type="application/json")