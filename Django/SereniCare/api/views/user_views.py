from rest_framework import generics
from accounts.models import CustomUser
from api.serializers.user_serializer import UserSerializer

class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
