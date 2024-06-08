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
    paginator = Paginator(prod_obj, 4)
    page = request.GET.get("page")
    prod_obj = paginator.get_page(page)

    context = {"prod_obj": prod_obj}
    return render(request, "shop/index.html", context)


def detail(request, id):
    prod_det = Products.objects.filter(id=id).first()
    context = {"details": prod_det}
    return render(request, "shop/detail.html", context)

def Checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")
        total = request.POST.get('amount', "")

        order = Order(item=items, name=name, email=email, address=address, city=city, state=state, zipcode=zip, total=total)
        order.save()
        
    return render(request, 'shop/checkout.html')