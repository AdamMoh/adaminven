from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Item
from main.forms import ItemForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse


def show_main(request):

    dataAll = Item.objects.all()
    dataCount = dataAll.count()
    
    context = {
        'appname': 'Adam Inventory',
        'name': 'Adam Muhammad',
        'class': 'KKI',
        'datas': dataAll,
        'dataCounts' : dataCount,
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")