from django.urls import path
from . import views

urlpatterns = [
    path('manufacturers/', views.ManufacturerList.as_view(), name='manufacturer_list'),
    path('manufacturers/new/', views.ManufacturerCreate.as_view(), name="manufacturer_create"),
    path('manufacturers/<int:pk>/', views.ManufacturerDetail.as_view(), name="manufacturer_detail"),
    path('manufacturers/<int:pk>/update',views.ManufacturerUpdate.as_view(), name="manufacturer_update"),
    path('manufacturers/<int:pk>/delete',views.ManufacturerDelete.as_view(), name="manufacturer_delete"),
    path('manufacturers/<int:pk>/modules/new/', views.ModuleCreate.as_view(), name="module_create")
]