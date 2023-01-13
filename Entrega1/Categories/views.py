from django.shortcuts import render
from django.http import HttpResponse
from Categories.models import Category
from Categories.forms import CategoryForm

def inicio(request):

    return render(request, "Categories/inicio.html")

def add_category(request):
        if request.method == 'GET':
            context = {
                'form': CategoryForm()
            }

            return render(request, 'Categories/add_categories.html', context=context)

        elif request.method == 'POST':

            form = CategoryForm(request.POST)
            if form.is_valid():
                Category.objects.create(
                    name=form.cleaned_data['name']
            )
            context = {
                'message': 'Categoria creada exitosamente'
            }
            return render(request, "Categories/add_categories.html", context=context)

        else: 
            context = {
                'form_errors': form.errors,
                'form': CategoryForm()
            }
            return render(request, 'Categories/add_categories.html', context=context)


def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'Categories/list_categories.html', context=context)