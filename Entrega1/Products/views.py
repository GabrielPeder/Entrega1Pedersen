from django.shortcuts import render
from django.http import HttpResponse
from Products.models import Product
from Products.forms import ProductForm

def inicio(request):

    return render(request, "Products/inicio.html")

def add_product(request):
        if request.method == 'GET':
            context = {
                'form': ProductForm()
            }

            return render(request, 'Products/add_product.html', context=context)

        elif request.method == 'POST':

            form = ProductForm(request.POST)
            if form.is_valid():
                Product.objects.create(
                    name=form.cleaned_data['name'],
                    model=form.cleaned_data['model'],
                    price=form.cleaned_data['price'],
                    stock=form.cleaned_data['stock']
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, "Products/add_product.html", context=context)

        else: 
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'Products/add_product.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'Products/list_products.html', context=context)

def searchform(request):

    if  request.GET['name']:

        
            name = request.GET['name'] 
        

            return render(request, "Products/search-results.html", {"name":name})

    else: 
            respuesta = "No enviaste datos"
    return HttpResponse(respuesta)