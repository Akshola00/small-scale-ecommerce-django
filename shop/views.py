from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    prod_obj = Products.objects.all()
    context = {
       'prod_obj':prod_obj 
    }
    return render(request, 'shop/index.html', context)