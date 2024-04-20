
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    prod_obj = Products.objects.all()

    # search code
    item_name = request.GET.get("item-name")
    print("lorem ipsum dolor sit amet: v", item_name)
    if item_name != "" and item_name is not None:
        prod_obj = prod_obj.filter(title__icontains=item_name)

   # paginator code
    paginator =Paginator(prod_obj, 4)
    

    context = {"prod_obj": prod_obj}
    return render(request, "shop/index.html", context)
