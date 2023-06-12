from django.contrib import admin
from django.urls import path
from car_app.views import ManagementPanelView, AddCarView, UpdateCarsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ManagementPanelView.as_view(), name="management_panel"),
    path("add/", AddCarView.as_view(), name="add_car"),
    path("update/", UpdateCarsView.as_view(), name="update_cars"),
]
