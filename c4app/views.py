from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from c4app.forms import UserForm,UserProfileInfoForm
# Create your views here.
from .models import *
import razorpay
from code4.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout



def home(request):
    return render (request,'c4app/home.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered=False

    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic= request.FILES['profile_pic']
            profile.save()

            registered= True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render (request,'c4app/reg.html',
         {'user_form':user_form,
            'profile_form':profile_form,
              'registered':registered})





def user_login(request):

      if request.method=='POST':
          username = request.POST.get('username')
          password= request.POST.get('password')

          user = authenticate(username=username,password=password)

          if user:
              if user.is_active:
                  login(request,user)
                  return render(request,'c4app/home.html')

              else :
                  return HttpResponse("NOT active")
          else:
              print("login attempt")
              print("username:{} and password {}".format(username,password))
              return HttpResponse ("invalid login details supplied!")
      else:
          return render(request,'c4app/login.html',{})


# @login_required
def php_course(request):
    return render(request, 'c4app/php_c.html')

# @login_required
def c_course(request):
    return render(request, 'c4app/c_c.html')

# @login_required
def cpp_course(request):
    return render(request, 'c4app/cpp_c.html')

# @login_required
def java_course(request):
    return render(request, 'c4app/java_c.html')

# @login_required
def html_course(request):
    return render(request, 'c4app/html_c.html')

# @login_required
def js_course(request):
    return render(request, 'c4app/js_c.html')

# @login_required
def python_course(request):
    return render(request, 'c4app/python_c.html')

# @login_required
def android_course(request):
    return render(request, 'c4app/android_c.html')






client=razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
def pay(request):
    order_amount=15000
    order_currency='INR'
    notes={'thank':"Goodluck champ"}

    payment_order=client.order.create(dict(amount=order_amount,currency=order_currency,notes=notes,payment_capture=1))
    payment_order_id=payment_order['id']
    context={
       'amount':1500 ,'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id
    }
    return render(request,'c4app/pay.html',context)


#def checkout(request):
 #if request.method=="POST":
#    items_json=request.POST.get('itemsJson', '')
#    name=request.POST.get('name','')
#    amount=request.POST.get('amount','')
#    email=request.POST.get('email','')
#    phone=request.POST.get('phone','')
#    city=request.POST.get('city','')
#    state=request.POST.get('state','')
#    order=Orders(items_json=items_json,amount=amount,name=name,email=email,phone=phone,city=city,state=state,)
#    update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
#    update.save()
#    thank=True
#    id=order.order_id
#    return render(request,'c4app/checkout.html',{'thank':thank,'id':id})
 #return render(request,c4app/checkout.html)
