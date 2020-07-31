from django.shortcuts import render
from .models import Product, Cart
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
 context={}
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
 
  