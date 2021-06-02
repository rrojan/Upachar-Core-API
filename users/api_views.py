from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Profile
from .serializers import RegisterSerializer, HospitalSerializer


class Register(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HospitalChoices(ViewSet):
    def list(self, request):
        queryset = Profile.objects.filter(user_type='hospital')
        serializer = HospitalSerializer(queryset, many=True)
        return Response(serializer.data)