from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Expenses
from django.db.models import Sum

# Create your views here.

def home(request):

    expense = Expenses.objects.all()

    total_items = expense.count()

    prices = Expenses.objects.aggregate(Sum('price'))

    for value in prices.values():
        prices = value

    context = {
        'expenses':expense,
        'total_items':total_items,
        'total_price':prices,
    }

    return render(request, 'cms_app/dashboard.html', context)

def add_item(request):

    if request.method=='POST':
        name = request.POST['item-name']
        price = request.POST['price']

        if Expenses.objects.filter(name=name).exists():
            messages.info(request,"Item already exists (choose another name)")
            return redirect('add')
        else:
            Expenses.objects.create(name=name.lower(),price=price.lower())
            return redirect('home')

    return render(request, 'cms_app/add_item.html')


def update_table(request):

    if request.method=='POST':
        name = request.POST['item-name']
        price = request.POST['price']

        if Expenses.objects.filter(name=name).exists():
            Expenses.objects.filter(name=name).update(name=name, price=price)
        else:
            messages.info(request, "Item doesn't exists")
            return redirect('update')

        return redirect('home')


    return render(request, 'cms_app/update.html')

    
def remove_items(request):

    if request.method=='POST':
        name = request.POST['item-name']

        if Expenses.objects.filter(name=name).exists():
            Expenses.objects.filter(name=name).delete()
            return redirect('home')
        else:
            messages.info(request, "Item doesn't exists")
            return redirect('remove')

    return render(request, 'cms_app/remove.html')


