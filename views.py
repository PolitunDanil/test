# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
# from users.forms import CustomUserCreationForm, LoginForm, UserEditForm, ProfileEditForm
# from users.models import CustomUser, Profile
# from django.contrib.auth.decorators import login_required
#
# # # Create your views here.
# # from django.views.decorators.csrf import csrf_exempt
# # from django.views.decorators.http import require_http_methods
# # import json
# #
# #
# # # def getUserFromDB(email):
# #     pass
# #
# # @csrf_exempt
# # @require_http_methods(["POST"])
# # def simple_api(request):
# #     res = {}
# #
# #     try:
# #         req = json.loads(request.body.decode("utf-8"))
# #     except Exception as e:
# #         res["details"] = "Invalid request body"
# #
# #     return HttpResponse(json.dumps({
# #         "message": "you authorized!"
# #     }), content_type="application/json")
# #
#
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = request.POST.get('email')
#             # password = request.POST.get('password')
#             # user = authenticate(username=username, password=password)
#             # profile = Profile.objects.create(user=user)
#             # user = authenticate(username=username, password=password)
#             # if user is not None:
#             #     find_usr_id = request.user.id
#             #     print('Ваш id', f"{find_usr_id}")
#             #     login(request, user)
#             # else:
#             #     HttpResponse('fuck you')
#         return take_id()
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})
#
# def take_id():
#     data_id = CustomUser.objects.latest('id')
#     print('Регистрация успешна, ваш ID' ,f"{data_id.id}")
#
#
# # @login_required
# def go_go(request):
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         profile = Profile.objects.create(user=user)
#         find_usr_id = request.user.id
#         print('Ваш id', f"{find_usr_id}")
#         login(request, user)
#         return HttpResponse("LOL")
#     else:
#         form = LoginForm(request.POST)
#     return render(request, 'login.html', {'form': form})
#
# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         # profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
#         # if user_form.is_valid() and profile_form.is_valid():
#         # find_usr_id = request.user.id
#         if user_form.is_valid():
#             user_form.save()
#             # try:
#             #     person = CustomUser.objects.get(id=find_usr_id)
#             #     person.delete()
#             #     return HttpResponseRedirect("/")
#             # except CustomUser.DoesNotExist:
#             #     return HttpResponse("Person not found")
#             # profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         # profile_form = ProfileEditForm(instance=request.user.profile)
#         return render(request,
#                       'edit.html',
#                       {'user_form': user_form})
#                        # 'profile_form': profile_form})
#
#
# # import json
# def delete(request):
#     find_usr_id = request.user.id
#     try:
#         person = CustomUser.objects.get(id=find_usr_id)
#         person.delete()
#         return HttpResponseRedirect("/")
#     except CustomUser.DoesNotExist:
#         return HttpResponse("Person not found")
#     # from django.http import JsonResponse
#     # return JsonResponse({'user.id': 'mydata'})
from rest_framework import permissions
from .models import CustomUser, Article, DropBox
from .serializers import (CustomUserSerializer, CustomUserUpdateSerializer, ArticleSerializer,
                          getAdminSerializer, DropBoxSerializer, FiltersSerializers)
from rest_framework import generics, views, parsers
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import login
from .permissions import IsAdminOrReadOnly,OnlyAdmin

class CustomUserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CustomUserListAPI(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)



class CustomUserDEL(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.IsAuthenticated,)


# class LoginView(views.APIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=self.request.data,
#             context={ 'request': self.request })
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return HttpResponse({"you authorized!"})

class CustomUserGET(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class getandpostArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)

class UpdateArticles(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAdminUser,)

class DestroyArticles(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAdminUser,)


class MakePermissions(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = getAdminSerializer
    permission_classes = (OnlyAdmin,)


class DropBoxViewset(generics.ListCreateAPIView):
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = (permissions.AllowAny,)

# class LinkUrl(views.APIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = DropBox.objects.all()
#
#     def post(self, request):
#         serializer = DropBoxSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         parser_classes = [parsers.MultiPartParser, parsers.FormParser]
#         return Response(serializer.data)
#
#     def put (self,  request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'write number id'})
#         try:
#             instance = DropBox.objects.get(pk=pk)
#         except:
#             return Response({'does not exist'})
#         serializer = DropBoxSerializer(data = request.data, instance=instance)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
#
#
#
#
# # можно сделать апи вью на пост и апдейт, залили - а в бд заменили фото на ссылку.
# class to_get_news_and_photo(views.APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#
#     def get(self, request):
#         a = Article.objects.all()
#         # return Response(ArticleSerializer(a, many = True).data)
#         p = DropBox.objects.all()
#         return Response[(DropBoxSerializer(p, many = True).data)(ArticleSerializer(a, many = True).data)]

class to_get_news_and_photo(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        filters = {}
        filters['model_1'] = Article.objects.all()
        filters['model_2'] = DropBox.objects.all()
        serializer = FiltersSerializers(filters)
        return Response (serializer.data)
