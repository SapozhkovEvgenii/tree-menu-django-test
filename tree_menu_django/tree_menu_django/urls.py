from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tree_menu/', include('tree_menu.urls')),
    path('admin/', admin.site.urls),
]
