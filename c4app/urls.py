from django.urls import path
from django.urls import include
from c4app import views
from django.contrib.auth import views as auth_views

app_name='c4app'

urlpatterns=[
 path('',views.home,name='home'),
 path('reg/',views.register,name='reg'),
 path('user_login/',views.user_login,name='user_login'),
 path('', include('django.contrib.auth.urls')),

 path('reset_password/',
 auth_views.PasswordResetView.as_view(template_name="c4app/password_reset.html"), name="reset_password"),

 path('reset_password_sent/',
       auth_views.PasswordResetDoneView.as_view(template_name="c4app/password_reset_sent"), name="reset_password_sent"),

 path('reset/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_forms"),name="password_reset_confirm"),

 path('reset_password_complete/',
       auth_views.PasswordResetCompleteView.as_view(template_name="c4app/password_reset_done"),name ="password_reset_complete"),

]
