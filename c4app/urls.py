from django urls import path
from c4app import views

urlpatterns=[
 path('',views.home,name='home')
]
