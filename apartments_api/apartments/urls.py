from django.contrib import admin
from django.urls import path, include
from .views import ApartmentsViews, ApartmentDetailView, UsersViews

urlpatterns = [
    path("", ApartmentsViews.as_view(), name="apartments_view"),
    path("apartments/<int:apart_id>",
         ApartmentDetailView.as_view(), name="apartment_view"),
    path("users/", UsersViews.as_view(), name="users_view")

]
