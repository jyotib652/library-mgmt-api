from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, DeleteAccount


urlpatterns = [
    # path('token-obtain/', obtain_auth_token, name='token_auth'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('get-details/', UserDetailAPI.as_view(), name='user-details'),
    path('delete-own-ac/<uuid:pk>/',DeleteAccount.as_view(), name='delete-own-account'),
    # path('login', AuthUserLoginView.as_view(), name='login'),
    # path('users', UserListView.as_view(), name='users_list'),
]