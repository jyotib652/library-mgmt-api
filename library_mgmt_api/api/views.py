from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework import mixins

from .serializers import (
    UserRegistrationSerializer,
    BookRegistrationSerializer,
    UserSerializer,
    RegisterSerializer
)

from .custom_permissions import AuthorAllStaffAllButEditOrReadOnly, MemberOnly

from .models import User, Book


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AuthorAllStaffAllButEditOrReadOnly,)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookRegistrationSerializer
    permission_classes = (AuthorAllStaffAllButEditOrReadOnly,)


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer

  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    
    return Response(serializer.data)


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key, 'username': serializer.instance.email}, status=status.HTTP_201_CREATED)


class DeleteAccount(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        email = user.email.rstrip()
        user_from_db = User.objects.get(email=email)
        given_id = user.id
        if given_id == user_from_db.id:
            user.delete()

        return Response({"result":"user deleted", 'status':status.HTTP_200_OK})


# class MemberViewBorrowReturnViewSet(mixins.ListModelMixin,
#                       mixins.UpdateModelMixin,
#                       viewsets.GenericViewSet):

#     queryset = Book.objects.all()
#     serializer_class = BookRegistrationSerializer
#     permission_classes = (MemberOnly,)

class MemberViewBorrowReturnViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookRegistrationSerializer
    permission_classes = (MemberOnly,)
    http_method_names = ['get', 'put', 'patch']