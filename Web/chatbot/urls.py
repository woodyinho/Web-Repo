from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import call_model



urlpatterns = [
    path('',call_model.as_view(),name ='refresh')

]