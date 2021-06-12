from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='login'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('signup',views.signup,name='signup'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_menu', views.admin_menu, name='admin_menu'),
    path('change_password', views.change_password, name='change_password'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('confirm_account',views.confirm_account,name='confirm_account'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('otp',views.otp,name='otp'),
    path('recipt',views.recipt,name='recipt'),
    path('otp1',views.otp1,name='otp1'),
    path('users_list',views.users_list,name='users_list'),
    path('product_list',views.product_list,name='product_list'),
    path('order_list',views.order_list,name='order_list'),
    path('details',views.details,name='details'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('buynow',views.buynow,name='buynow'),
    path('book',views.book,name='book'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('electronics',views.electronics,name='electronics'),
    path('jewellary',views.jewellary,name='jewellary'),
    path('computers',views.computers,name='computers'),
    path('edit',views.edit,name='edit'),
    path('edit_details',views.edit_details,name='edit_details'),
    path('logout',views.logout,name='logout'),
    path('cancel',views.cancel,name='cancel'),
    path('cancel1',views.cancel1,name='cancel1'),
    path('addproduct',views.addproduct,name='addproduct')
#path('edit1',views.edit1,name='edit1')
#path('editproduct',views.editproduct,name='editproduct'),





]