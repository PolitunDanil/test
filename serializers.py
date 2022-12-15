from rest_framework import serializers
from .models import CustomUser, Article, DropBox
import re
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class CustomUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','first_name', 'last_name', 'email', 'phone_number', 'password')


    def validate(self, data):
            if data['first_name']:
                v_name =  data['first_name']
                if re.search('[@,$,!,%,*,#,?,&]', v_name):
                    raise serializers.ValidationError({'error':'Ur name should not have @$!%*#?&'})

            if data['last_name']:
                v_surname = data['last_name']
                if re.search('[@,$,!,%,*,#,?,&]', v_surname):
                    raise serializers.ValidationError({'error': 'Ur surname should not have @$!%*#?&'})

            if data['phone_number']:
                clear_phone_number = data['phone_number']
                if re.search('[A-Z]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have letters'})
                if re.search('[a-z]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have letters'})
                if re.search('[@,$,!,%,*,#,?,&]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have @$!%*#?&'})

            if data['password']:
                clear_password = data['password']
                if re.search('[A-Z]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                if re.search('[0-9]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                if re.search('[a-z]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                data['password'] = make_password(data['password'])

            return data





class CustomUserUpdateSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','first_name', 'last_name', 'email', 'phone_number', 'password')

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(CustomUserUpdateSerializer, self).__init__(*args, **kwargs)


    def validate(self, data):

            if 'first_name' in data:
                v_name =  data['first_name']
                if re.search('[@,$,!,%,*,#,?,&]', v_name):
                    raise serializers.ValidationError({'error':'Ur name should not have @$!%*#?&'})

            if 'last_name' in data:
                v_surname = data['last_name']
                if re.search('[@,$,!,%,*,#,?,&]', v_surname):
                    raise serializers.ValidationError({'error': 'Ur surname should not have @$!%*#?&'})


            if 'phone_number' in data:
                clear_phone_number = data['phone_number']
                if re.search('[A-Z]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have letters'})
                if re.search('[a-z]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have letters'})
                if re.search('[@,$,!,%,*,#,?,&]', clear_phone_number):
                    raise serializers.ValidationError({'error': 'Ur phone should not have @$!%*#?&'})


            if 'password' in data:
                clear_password = data['password']
                if re.search('[A-Z]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                if re.search('[0-9]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                if re.search('[a-z]', clear_password)==None:
                    raise serializers.ValidationError({'error': 'Make good password, with A-z-1'})
                data['password'] = make_password(data['password'])
            return data


# class LoginSerializer(serializers.Serializer):
#
#     email = serializers.EmailField(
#         label="Email",
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         # style={'input_type': 'password'},
#         # trim_whitespace=False,
#         write_only=True
#     )
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#
#         if email and password:
#             user = authenticate(request=self.context.get('request'),
#                                 username=email, password=password)
#             if not user:
#                 msg = 'Access denied: wrong username or password.'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Both "username" and "password" are required.'
#             raise serializers.ValidationError(msg, code='authorization')
#         attrs['user'] = user
#         return attrs

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields ='__all__'
        # fields =('id','news')

class getAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('is_superuser',)


class DropBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = DropBox
        fields = '__all__'

class FiltersSerializers(serializers.Serializer):
    model_1 = ArticleSerializer(read_only=True, many=True)
    model_2 = DropBoxSerializer(read_only=True, many=True)
