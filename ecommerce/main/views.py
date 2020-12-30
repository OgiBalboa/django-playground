from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Item, OrderedItem, Order
from django.views import generic
from django.utils import timezone
class HomeView(generic.ListView):
    model = Item
    template_name = "home-page.html"
#------------ PRODUCT PAGE -------------
class ProductPage(generic.DetailView):
    model = Item
    template_name = "product-page.html"
    
def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    ordered_item,_ = OrderedItem.objects.get_or_create(item=item, customer=request.user,ordered=False)
    # If user matches with auth user and order not completed 
    query = Order.objects.filter(customer = request.user, ordered = False)
    if query.exists():                                                  
        order = query[0] #Grab the order
        # check if the order item is in the order
        if order.items.filter(item__slug = item.slug).exists(): #Does order contains this item
            ordered_item.quantity += 1
            ordered_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("main:product", slug=slug)
        else:
            order.items.add(ordered_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("main:product", slug=slug)
    else:
        order = Order.objects.create(customer = request.user,order_date = timezone.now())
        order.items.add(ordered_item)
        order.save()
        messages.info(request, "This item was added to your cart.")
        return redirect("main:product", slug=slug)

def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        customer=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderedItem.objects.filter(
                item=item,
                customer=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            #return redirect("main:order-summary")
            return redirect("main:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("main:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("main:product", slug=slug)
#------------------------------------------    
class CheckOutPage(generic.DetailView):
    pass