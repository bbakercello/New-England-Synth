from django.urls import path
from . import views

urlpatterns = [
    path('manufacturers/', views.ManufacturerList.as_view(), name='manufacturer_list'),
    path('manufacturers/new/', views.ManufacturerCreate.as_view(), name="manufacturer_create"),
]