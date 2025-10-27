from django.shortcuts import render


def index(request):
    ctx = {
    }
    return render(request, 'index.html', ctx)


def product(request):
    ctx = {
    }
    return render(request, 'product.html', ctx)


def contacts(request):
    ctx = {
    }
    return render(request, 'contacts.html', ctx)


def compare(request):
    ctx = {
    }
    return render(request, 'compare.html', ctx)


def catalog(request):
    ctx = {
    }
    return render(request, 'catalog.html', ctx)


def cart(request):
    ctx = {
    }
    return render(request, 'cart.html', ctx)
