import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound,JsonResponse
from main.models import Item
from main.forms import ItemForm, LoginForm, SignUpForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def show_main(request):

    dataAll = Item.objects.filter(user=request.user)
    dataCount = dataAll.count()
    
    context = {
        'appname': 'Adam Inventory',
        'name': 'Adam Muhammad',
        'class': 'KKI',
        'datas': dataAll,
        'dataCounts' : dataCount,
        'last_login': datetime.datetime.strptime(request.COOKIES['last_login'], '%Y-%m-%d %H:%M:%S.%f'),
    }

    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
         'last_login': datetime.datetime.strptime(request.COOKIES['last_login'], '%Y-%m-%d %H:%M:%S.%f'),
         }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()
    msg = None
    # success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    context = {"form": form, "msg": msg}
    return render(request, "register.html", context)

def login_user(request):

    form = LoginForm(request.POST or None)

    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            msg = messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {"form": form, "msg": msg}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def delete_item(request, id):
    try:
        data = Item.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    except Item.DoesNotExist:
        return HttpResponse(status=204)
    
@login_required(login_url='/login')
def delete_item_ajax(request, id):
    try:
        data = Item.objects.get(id=id)
        data.delete()
        return HttpResponse(b"OK", status=201)
    except Item.DoesNotExist:
        return HttpResponse(status=204)

@login_required(login_url='/login')
def increment_item(request, id):
    data = Item.objects.get(id=id)
    data.amount += 1
    data.save()

    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def decrement_item(request, id):
    data = Item.objects.get(id=id)
    data.amount -= 1

    if data.amount == 0:
        data.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        data.save()
        return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def edit_item(request, id):
    data = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=data)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form, 'last_login': datetime.datetime.strptime(request.COOKIES['last_login'], '%Y-%m-%d %H:%M:%S.%f'),}
    return render(request, "edit.html", context)
    

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        category = request.POST.get("category")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, category=category,price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            category = data["category"],
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)