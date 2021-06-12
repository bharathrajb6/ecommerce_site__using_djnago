from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import smtplib
import string
import random as ra
from .models import products,orders,carts,tracks

email1=''
fname=''
lname=''
password=''
usernames=''
r=''


def home(request):
    return render(request,'home.html')

def about(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("bharathsr2001@gmail.com", "Bharath@B26")
        message ="Contact \n\nName : {}\nEmail : {}\n\n{}".format(name, email, msg)
        s.sendmail(email, "bharathsr2001@gmail.com", message)
        s.quit()
        messages.success(request, 'Successfully Sent')
        return redirect('about')
    else:
        return render(request,'about.html')


def product(request):
    pr=products.objects.all()
    return render(request,'product.html',{'data':pr})

def contact(request):
    global usernames
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg=request.POST['message']
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("bharathsr2001@gmail.com", "Bharath@B26")
            message = "Contact \n\nName : {}\nEmail : {}\nTelephone : {}\n{}".format(name,email,phone,msg)
            s.sendmail(email,"bharathsr2001@gmail.com", message)
            s.quit()
            messages.success(request,'Successfully Sent')
            return redirect('contact')
        except:
            messages.success(request, 'Unable to Sent')
            return redirect('contact')
    else:
        user=User.objects.filter(username=usernames)
        return render(request,'contact.html',{'data':user})

def profile(request):
    global usernames

    user=User.objects.get(username=usernames)
    c=orders.objects.filter(user=user)
    c1=len(list(c))
    return render(request,'profile.html',{'data':user,'k':c1})



def login(request):
    global usernames
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            usernames=username
            messages.success(request,'Welcome '+username)
            return redirect('home')
        else:
            messages.success(request, 'Username or Password is not exist')
            return redirect('login')
    else:
        return render(request,'login.html')

def signup(request):
    global email1,fname,lname,usernames,password
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2 = request.POST['password2']
        email1=email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Exists')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username Exists')
            return redirect('signup')
        elif pass1!=pass2:
            messages.error(request, 'Password is not matching')
            return redirect('signup')
        elif fname.isnumeric() or lname.isnumeric():
            messages.error(request, 'Name cannot be integer')
            return redirect('signup')
        elif len(pass1)<8 or len(pass2)<8:
            messages.error(request, 'Password length should be 8 or more')
            return redirect('signup')
        else:
            fname=fname
            lname=lname
            password=pass1
            usernames=username
            return redirect('confirm_account')
    else:
        return render(request,'signup.html')


def admin_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password= request.POST['password']
        if username=='admin' and password=='bharath':
            messages.success(request,'Welcome Admin')
            return redirect('admin_menu')
        else:
            messages.error(request,'Username or Password is not exist')
            return redirect('admin_login')
    else:
        return render(request,'admin_login.html')


def admin_menu(request):
    return render(request,'admin_menu.html')

def cart(request):
    u = User.objects.get(username=usernames)
    pr1 = carts.objects.filter(user=u)
    return render(request, 'cart.html', {'data': pr1})


def change_password(request):
    global usernames
    if request.method=='POST':
        p1=request.POST['p1']
        p2=request.POST['password']
        try:
            u = User.objects.get(username=usernames)
        except:
            u=None
        if u is not None:
            if p1==p2:
                u.set_password(p1)
                u.save()
                auth.login(request,u)
                messages.success(request,'Password is changed successfully.')
                return redirect('home')
            else:
                messages.success(request,'Mismatched Password')
                return redirect('change_password')
        else:
            messages.success(request, 'Username is not found.')
            return redirect('change_password')
    else:
        return render(request,'change_password.html')

def confirm_account(request):
    global r
    if request.method == "POST":
        number=ra.randint(100000,1000000)
        r=number
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("bharathsr2001@gmail.com", "Bharath@B26")
        message = "Confirm Your Account\n\nOTP : {}".format(number)
        s.sendmail("bharathsr2001@gmail.com", email1, message)
        s.quit()
        return redirect('otp')
    else:
        return render(request,'confirm_account.html')

def order(request):
    u=User.objects.get(username=usernames)
    o2=orders.objects.filter(user=u)
    return render(request,'order.html',{'data':o2})


def otp(request):
    global email1,fname,lname,usernames,password,r
    if request.method=="POST":
        n1 = request.POST['n1']
        n2 = request.POST['n2']
        n3=request.POST['n3']
        n4 = request.POST['n4']
        n5 = request.POST['n5']
        n6 = request.POST['n6']
        if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
            n=int(n1+n2+n3+n4+n5+n6)
            if n==r:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email1, username=usernames,
                                            password=password)
                user.save()
                messages.error(request, 'User is created successfully')
                return redirect('home')
        else:
            messages.error(request,'OTP is wrong')
            return redirect('otp')
    else:
        return render(request,'otp.html')
def edit(request):
    global usernames
    if request.method=="POST":
        ono=request.POST['ono']
        obj=orders.objects.get(ord_no=ono)
        return render(request,'edit.html',{'data':obj})



def edit1(request):
    global usernames
    if request.method=="POST":
        pid=request.POST['pid']
        obj=products.objects.get(pid=pid)
        return render(request,'edit1.html',{'data':obj})

def edit_details(request):
    if request.method=='POST':
        ono=request.POST['ono']
        status=request.POST['status']
        obj=orders.objects.get(ord_no=ono)
        obj.status=status
        obj.save()
        messages.success(request,'Done')
        return redirect('order_list')

def logout(request):
    auth.logout(request)
    return redirect('login')

def wishlist(request):
    return render(request,'wishlist.html')

def forgot_password(request):
    global r
    if request.method=="POST":
        email=request.POST['email']
        number = ra.randint(100000, 1000000)
        r = number
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("bharathsr2001@gmail.com", "Bharath@B26")
        message = "Reset Your Password\n\nOTP : {}".format(number)
        s.sendmail("bharathsr2001@gmail.com", email, message)
        s.quit()
        return redirect('otp1')
    else:
        return render(request,'forgot_password.html')

def otp1(request):
    if request.method=="POST":
        n1=request.POST['n1']
        n2 = request.POST['n2']
        n3 = request.POST['n3']
        n4 = request.POST['n4']
        n5 = request.POST['n5']
        n6 = request.POST['n6']
        if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
            n = int(n1 + n2 + n3 + n4 + n5 + n6)
            if n == r:
                return redirect('change_password')
        else:
            messages.error(request,'OTP is wrong')
            return redirect('otp1')
    else:
        return render(request,'otp1.html')


def users_list(request):
    u=User.objects.exclude(username='bharath')
    return render(request,'users_list.html',{'data':u})

def product_list(request):
    u=products.objects.all()
    return render(request,'product_list.html',{'data':u})


def addproduct(request):
    if request.method=="POST":
        name=request.POST['name']
        category=request.POST['category']
        img=request.POST['img']
        print(img)
        desc=request.POST['desc']
        price = request.POST['price']
        pid=ra.randint(1,10000000)
        p1=products(pid=pid,category=category,pname=name,pimg=img,pdisc=desc,price=price)
        p1.save()
        print('Success')
        return redirect('product_list')
    else:
        return render(request,'addproduct.html')
'''
def editproduct(request):
    if request.method=="POST":
        pid=request.POST['pid']
        name=request.POST['name']
        img = request.POST['image']
        desc = request.POST['desc']
        price = request.POST['price']
        obj=products.objects.get(pid=pid)
        obj.pname=name
        obj.pimg=img
        obj.pdisc=desc
        obj.price=price
        obj.save();
        return redirect('product_list')

'''
def order_list(request):
    u=orders.objects.all()
    return render(request,'order_list.html',{'data':u})

def details(request):
    if request.method=="POST":
        pid=request.POST['productid']
        pr=products.objects.all()
        for i in pr:
            if i.pid==pid:
                break
        return render(request,'details.html',{'data':i})

def addtocart(request):
    global usernames
    if request.method=="POST":
        pid1=request.POST['productid']
        cid=ra.randint(100,10000000000)
        if carts.objects.filter(cid=cid).exists():
            cid = ra.randint(100, 10000000000)
        users=User.objects.get(username=usernames)
        pid2=products.objects.get(pid=pid1)
        if carts.objects.filter(pid=pid2).exists():
            messages.error(request, 'Item is already there in your cart')
            return redirect('home')
        else:
            c=carts(user=users,pid=pid2,cid=cid)
            c.save()
            messages.error(request, 'Successfully added to cart')
            return redirect('home')

def buynow(request):
    if request.method == "POST":
        pid1 = request.POST['productid']
        pr = products.objects.all()
        for i in pr:
            if i.pid == pid1:
                break
        return render(request, 'buynow.html', {'data': i})

def recipt(request):
    global usernames
    N = 10
    if request.method == "POST":
        pid1 = request.POST['productid']
        fname=request.POST['firstname']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        q1=request.POST['quantity']
        us=usernames
        ono = ''.join(ra.choices(string.ascii_uppercase + string.digits, k=N))
        users = User.objects.get(username=us)
        pid2 = products.objects.get(pid=pid1)
        p=pid2.price
        total=p*int(q1)
        address="{},{},{},{}".format(address,city,state,pincode)
        o1=orders(user=users,pid=pid2,ord_no=ono,quantity=q1,amount=total,address=address,status='Registered')
        o1.save()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("bharathsr2001@gmail.com", "Bharath@B26")
        message = "Your order has been placed\nOrder ID : {}".format(ono)
        s.sendmail("bharathsr2001@gmail.com", email, message)
        s.quit()
        messages.error(request, 'Your order has been placed')
        on=orders.objects.filter(ord_no=ono)
        return render(request,'recipt.html',{'datas':on})

def book(request):
    obj=products.objects.filter(category='book')
    return render(request,'product.html',{'data':obj})

def mobiles(request):
    obj=products.objects.filter(category='mobiles')
    return render(request,'product.html',{'data':obj})

def computers(request):
    obj=products.objects.filter(category='computers')
    return render(request,'product.html',{'data':obj})

def jewellary(request):
    obj=products.objects.filter(category='jewellary')
    return render(request,'product.html',{'data':obj})

def electronics(request):
    obj=products.objects.filter(category='electronics')
    return render(request,'product.html',{'data':obj})

def cancel(request):
    if request.method=='POST':
        ono=request.POST['ono']
        obj=orders.objects.get(ord_no=ono)
        if obj.status=='Shipped' or obj.status=='Out for delivery' or obj.status=='Paid and Delivered':
            messages.error(request,'Unable to cancel your order')
            return redirect('order')
        else:
            obj.delete()
            messages.success(request,'Order is cancelled')
            return redirect('order')


def cancel1(request):
    if request.method=='POST':
        cno=request.POST['cno']
        obj=carts.objects.get(cid=cno)
        obj.delete()
        messages.success(request,'Item is removed from your cart')
        return redirect('cart')





