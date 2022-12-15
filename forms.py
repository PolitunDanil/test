# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from users.models import CustomUser, Profile
# from django.core.exceptions import ValidationError
# import re
# from django.contrib.auth.forms import AuthenticationForm
#
#
#
# class CustomUserCreationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=50, min_length=3, required=True)
#     last_name = forms.CharField(max_length=50, min_length=3, required=True)
#     email = forms.EmailField(max_length=254, required=True)
#     phone_number = forms.CharField(max_length=11, min_length =7, required=True)
#
#
#
#     def clean_email(self):
#         new_email = self.cleaned_data['email']
#         if CustomUser.objects.filter(email=new_email).exists():
#             raise ValidationError('You cannot reuse the same email')
#         return new_email
#
#     def clean_first_name(self):
#         clear_first_name = self.cleaned_data['first_name']
#         if re.search('[@,$,!,%,*,#,?,&]', clear_first_name):
#             raise ValidationError('Ur name should not have @$!%*#?&')
#         return clear_first_name
#
#     def clean_last_name(self):
#         clear_last_name = self.cleaned_data['last_name']
#         if re.search('[@,$,!,%,*,#,?,&]', clear_last_name):
#             raise ValidationError('Ur name should not have @$!%*#?&')
#         return clear_last_name
#
#
#
#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
#
#     def clean_password1(self):
#         clear_password = self.cleaned_data['password1']
#         if re.search('[A-Z]', clear_password)==None and re.search('[0-9]', clear_password)==None and re.search('[a-z]', clear_password)==None:
#             raise ValidationError('use numeric')
#         return clear_password
#
#     def clean_phone_number(self):
#         clear_phone_number = self.cleaned_data['phone_number']
#         if re.search('[A-Z]', clear_phone_number) and re.search('[a-z]', clear_phone_number) and re.search('[@,$,!,%,*,#,?,&]', clear_phone_number):
#             raise ValidationError('Ur phone should not have letters')
#         return clear_phone_number
#
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta(UserChangeForm):
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=50, min_length=3, required=True)
#     password = forms.CharField(max_length=50, min_length=3, required=True)
#
#
# # class UpdateUserForm(CustomUserCreationForm):
# #     email = forms.EmailField(required=True,
# #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     password = forms.CharField(max_length=50,
# #                                required=True,
# #                                widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     last_name = forms.CharField(max_length=100,min_length=3,
# #                                required=True,
# #                                widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     first_name = forms.CharField(max_length=100,min_length=3,
# #                                required=True,
# #                                widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     phone_number = forms.CharField(max_length=11,min_length=7,
# #                                  required=True,
# #                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
# #
# #     class Meta:
# #         model = CustomUser
# #         fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
# #
# #
# # class UpdateProfileForm(forms.ModelForm):
# #     email = forms.EmailField(required=True,
# #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     password = forms.CharField(max_length=50,
# #                                required=True,
# #                                widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     last_name = forms.CharField(max_length=100, min_length=3,
# #                                 required=True,
# #                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     first_name = forms.CharField(max_length=100, min_length=3,
# #                                  required=True,
# #                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     phone_number = forms.CharField(max_length=11, min_length=7,
# #                                    required=True,
# #                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
# #
# #     class Meta:
# #         model = CustomUser
# #         fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
#
#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
#
#         def clean_email(self):
#             new_email = self.cleaned_data['email']
#             if CustomUser.objects.filter(email=new_email).exists():
#                 raise ValidationError('You cannot reuse the same email')
#             return new_email
#
#         def clean_first_name(self):
#             clear_first_name = self.cleaned_data['first_name']
#             if re.search('[@,$,!,%,*,#,?,&]', clear_first_name):
#                 raise ValidationError('Ur name should not have @$!%*#?&')
#             return clear_first_name
#
#         def clean_last_name(self):
#             clear_last_name = self.cleaned_data['last_name']
#             if re.search('[@,$,!,%,*,#,?,&]', clear_last_name):
#                 raise ValidationError('Ur name should not have @$!%*#?&')
#             return clear_last_name
#
#         def clean_password(self):
#             clear_password = self.cleaned_data['password']
#             if re.search('[A-Z]', clear_password) == None and re.search('[0-9]', clear_password) == None and re.search(
#                     '[a-z]', clear_password) == None:
#                 raise ValidationError('use numeric')
#             return clear_password
#
#         def clean_phone_number(self):
#             clear_phone_number = self.cleaned_data['phone_number']
#             if re.search('[A-Z]', clear_phone_number) and re.search('[a-z]', clear_phone_number) and re.search(
#                     '[@,$,!,%,*,#,?,&]', clear_phone_number):
#                 raise ValidationError('Ur phone should not have letters')
#             return clear_phone_number
#
# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
#
# # class DeactivateUserForm(forms.ModelForm):
# #     class Meta:
# #         model = CustomUser
# #         fields = ['is_active']