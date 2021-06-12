from django.db import models as mo


# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class products(mo.Model):
    pid=mo.CharField(max_length=10,default='',primary_key=True)
    category=mo.CharField(max_length=50,default='')
    pname=mo.CharField(max_length=100,default='')
    pimg=mo.ImageField(default='')
    pdisc=mo.TextField(max_length=200,default='')
    price=mo.IntegerField(default=0)

    def __str__(self):
        return self.pid

class orders(mo.Model):
    user=mo.ForeignKey(to=User,on_delete=mo.CASCADE)
    pid=mo.ForeignKey(to=products,on_delete=mo.CASCADE)
    ord_no=mo.CharField(max_length=50,default='',primary_key=True)
    quantity=mo.IntegerField(default=0)
    amount=mo.FloatField(default=0)
    address=mo.TextField(max_length=500,default='')
    status = mo.CharField(max_length=50, default='')
    def __str__(self):
        return self.ord_no

class carts(mo.Model):
    user=mo.ForeignKey(to=User,on_delete=mo.CASCADE)
    pid=mo.ForeignKey(to=products,on_delete=mo.CASCADE)
    cid=mo.CharField(default='',max_length=50,primary_key=True)
    def __str__(self):
        return self.cid

class tracks(mo.Model):
    user=mo.ForeignKey(to=User,on_delete=mo.CASCADE)
    pid=mo.ForeignKey(to=products,on_delete=mo.CASCADE)
    ord_no=mo.ForeignKey(to=orders,on_delete=mo.CASCADE,default='')
    tid=mo.CharField(default='',max_length=50,primary_key=True)
    def __str__(self):
        return self.tid

class wishlist(mo.Model):
    user=mo.ForeignKey(to=User,on_delete=mo.CASCADE)
    pid=mo.ForeignKey(to=products,on_delete=mo.CASCADE)
    wid=mo.CharField(default='',max_length=50,primary_key=True)
    def __str__(self):
        return self.wid
