from django.shortcuts import render
from .models import Product, Cart
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect) 
# Create your views here.
# cart fuctions
def repeat(request):
 carts=Cart.objects.filter(cartuser=request.user)
 total_price=0
 total_items=0
 for x in carts:
  total_price=total_price+x.price
  total_items=total_items+1
 return total_items
# 

def store(request):
 carts=Cart.objects.all()
 products=Product.objects.all()
 context={'products':products, 'total_items_in_cart':repeat(request), 'carts':carts}
 return render(request, 'store/store.html', context)

def cart(request):
 carts=Cart.objects.filter(cartuser=request.user)
 total_price=0
 total_items=0
 for x in carts:
  total_price=total_price+x.price
  total_items=total_items+1
 context={'carts':carts, 'price':total_price, 'items':total_items, 'total_items_in_cart':total_items}
 return render(request, 'store/cart.html', context)

def checkout(request):
 carts=Cart.objects.filter(cartuser=request.user)
 total_price=0
 total_items=0
 for x in carts:
  total_price=total_price+x.price
  total_items=total_items+1

 context={'carts':carts, 'total_price':total_price, 'total_items':total_items, 'total_items_in_cart':repeat(request)}
 return render(request, 'store/checkout.html', context)

# -------------adding to cart list store id of all products already in cart-------------------------


def addtocart(request, slag):
 
 
  
  repeat(request)
  
  item=Product.objects.get(pk=slag)
  # --------------to check if item already presentd in cart-------------------------------
  name=item.product_name
  carts=Cart.objects.filter(cartuser=request.user)
  for cart in carts:
   if cart.name==name:
    products=Product.objects.all()
    context={'products':products, 'total_items_in_cart':repeat(request), }
    return render(request, 'store/store.html', context)
    
  # --------------else adding to cart------------------------------
  add=Cart(name=item.product_name, price=item.product_price, img=item.product_img, cartuser=request.user,)
  add.save()
  products=Product.objects.all()
  context={'products':products, 'total_items_in_cart':repeat(request), }
  return render(request, 'store/store.html', context)
 
def delete_item(request, id):
       
    # fetch the object related to passed id 
    obj = get_object_or_404(Cart, id = id) 
    context ={'obj':obj, 'total_items_in_cart':repeat(request)}
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/cart") 
  
    return render(request, "store/delete_item.html", context) 