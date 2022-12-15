from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, Profile, Article, DropBox

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'password']
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone_number', 'password']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article)
admin.site.register(DropBox)