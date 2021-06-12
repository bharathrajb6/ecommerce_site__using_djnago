from django.contrib import admin
from ecom.models import products,orders,carts,tracks,wishlist

# Register your models here.
admin.site.register(products)
admin.site.register(orders)
admin.site.register(carts)
admin.site.register(tracks)
admin.site.register(wishlist)