from django.contrib import admin
from c4app.models import UserProfileInfo
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User


# Register your models here.
admin.site.register(UserProfileInfo)
