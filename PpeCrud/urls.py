
from django.contrib import admin
from django.urls import path

from etud.views import index, delete_data, update_data

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:id>/', delete_data, name="deletedata"),
    path('<int:id>/', update_data, name="updatedata"),
    path('admin/', admin.site.urls),
]
