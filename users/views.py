from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer


class ProfileView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    return Response({"username": user.username})