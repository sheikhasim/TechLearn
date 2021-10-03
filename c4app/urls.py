from django.urls import path
from django.urls import include
from c4app import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name='c4app'

urlpatterns=[
 path('',views.home,name='home'),
 path('user_login/',views.user_login,name='login'),
 path('reg/',views.register,name='reg'),
 path('php_c/',views.php_c,name='php_c'),
 path('c_c/',views.c_c,name='c_c'),
 path('cpp_c/',views.cpp_c,name='cpp_c'),
 path('java_c/',views.java_c,name='java_c'),
 path('html_c/',views.html_c,name='html_c'),
 path('js_c/',views.js_c,name='js_c'),
 path('python_c/',views.python_c,name='python_c'),
 path('android_c/',views.android_c,name='android_c'),
 path('', include('django.contrib.auth.urls')),
 path('play/',views.play,name='play'),

 path('reset_password/',
 auth_views.PasswordResetView.as_view(template_name="c4app/password_reset.html"), name="reset_password"),

 path('reset_password_sent/',
       auth_views.PasswordResetDoneView.as_view(template_name="c4app/password_reset_sent"), name="reset_password_sent"),

 path('reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_forms"),name="password_reset_confirm"),

 path('reset_password_complete/',
       auth_views.PasswordResetCompleteView.as_view(template_name="c4app/password_reset_done"),name ="password_reset_complete"),
 path('accounts/',include('allauth.urls')),
 #path('pay/',views.pay,name='pay'),


]
