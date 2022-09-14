from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    list_item = CatalogItem.objects.all()
    context = {
    'list_item': list_item,
    'nama' : 'Alifia',
    'NPM': '2106634723'
}
    return render(request, "katalog.html", context)

