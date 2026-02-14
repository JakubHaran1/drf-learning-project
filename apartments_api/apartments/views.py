
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render

from .models import ApartmentModel, User
from .serializers import ApartmentSerializer, UserSerializer
from .filters import ApartFilter
# ApiViev part


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


# GenericViews + mixins
class ApartmentsGenericView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApartmentDetailGenericView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = ApartmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        apart_id = self.kwargs['id']
        return ApartmentModel.objects.filter(id=apart_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = ApartmentModel.objects.all()
    filterset_class = ApartFilter
    pagination_class = PageNumberPagination

    pagination_class.max_page_size = 3
    pagination_class.page_size_query_param = 'size'

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
