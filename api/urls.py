from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, DeleteAccountAPIView


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('get-details/', UserDetailAPI.as_view(), name='user-details'),
    path('delete-own-ac/<uuid:pk>/',DeleteAccountAPIView.as_view(), name='delete-own-account'),
]