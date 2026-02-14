from django.contrib import admin
from django.urls import path, include
from .views import ApartmentsViews, ApartmentDetailView, UsersViews, ApartmentsGenericView, ApartmentDetailGenericView, ApartmentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", ApartmentsGenericView.as_view(), name="apartments_view"),
    path("apartments/<int:id>",
         ApartmentDetailGenericView.as_view(), name="apartment_view"),
    path("users/", UsersViews.as_view(), name="users_view"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
router = DefaultRouter()
router.register('apartmentsViewSet', ApartmentViewSet)
urlpatterns += router.urls
