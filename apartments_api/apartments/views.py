
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import render

from .models import ApartmentModel, User
from .serializers import ApartmentSerializer, UserSerializer


class ApartmentsViews(APIView):
    def get(self, request):
        apartments = ApartmentModel.objects.all()
        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ApartmentDetailView(APIView):
    def get(self, request, apart_id):
        try:
            apartment = ApartmentModel.objects.get(id=apart_id)
        except ApartmentModel.DoesNotExist:
            raise NotFound(apartment)
        serializer = ApartmentSerializer(apartment)

        return Response(serializer.data)
    
    
    



class UsersViews(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# Create your views here.
