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
 path('php_c/',views.php_course,name='php_course'),
 path('c_c/',views.c_course,name='c_course'),
 path('cpp_c/',views.cpp_course,name='cpp_course'),
 path('java_c/',views.java_course,name='java_course'),
 path('html_c/',views.html_course,name='html_course'),
 path('js_c/',views.js_course,name='js_course'),
 path('python_c/',views.python_course,name='python_course'),

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
