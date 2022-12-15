from django.contrib import admin
from django.urls import path
from users import views as core_views
from users.views import (CustomUserUpdate,CustomUserListAPI, CustomUserDEL, CustomUserGET,
getandpostArticles, UpdateArticles, DestroyArticles, MakePermissions, DropBoxViewset, to_get_news_and_photo)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('update/<int:pk>/', CustomUserUpdate.as_view()),
    path('registration/', CustomUserListAPI.as_view()),
    path('delete/<int:pk>/', CustomUserDEL.as_view()),
    path('check/', getandpostArticles.as_view()),
    path('upcheck/<int:pk>/', UpdateArticles.as_view()),
    path('delcheck/<int:pk>/', DestroyArticles.as_view()),
    path('make/<int:pk>/', MakePermissions.as_view()),
    path('try/', DropBoxViewset.as_view()),
    path('get/', to_get_news_and_photo.as_view()),
    # path('login/', LoginView.as_view()),
    path('get/', CustomUserGET.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('registration/', core_views.signup, name='signup'),
    # # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', core_views.go_go, name = 'login'),
    # path('profile/', core_views.edit, name = 'edit'),
    # # path('profile/', core_views.Change_profile, name = 'profile'),
    # # path('profile/', Profile_show.as_view(), name = 'profile'),
    # # path('profile/<int:pk>/', Profile_show.as_view(), name='profile'),
    # path('delete/', core_views.delete, name = 'delete'),
    # # path('create_profile/', CreateProfilePageView.as_view(), name = 'create_profile'),
]
