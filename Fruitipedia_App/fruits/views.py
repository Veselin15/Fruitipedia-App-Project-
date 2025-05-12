from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fruit, Category
from .forms import CategoryForm, FruitAddForm, FruitEditForm, DeleteFruitForm
# Create your views here.
def index(request):
    return render(request, 'common/index.html')
def dashboard(request):
    fruits = Fruit.objects.all()
    context = {'fruits': fruits}
    return render(request, 'common/dashboard.html', context)
def create_fruit(request):
    if request == 'GET':
        form = FruitAddForm()
    else:
        form = FruitAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}


    return render(request, 'fruits/create-fruit.html', context)
def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)
def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.save()
            return redirect('dashboard')
    context = {'form': form, 'fruit': fruit}
    return render(request, 'fruits/edit-fruit.html', context)
def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    context = {'form': form, 'fruit': fruit}

    return render(request, 'fruits/delete-fruit.html',context)
def create_category(request):
    if request.method == 'GET':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}

    return render(request, 'categories/create-category.html', context)