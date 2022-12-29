from tree_menu.views import all_menu

from django.urls import path


urlpatterns = [
    path('', all_menu, name='index'),
    path('<slug:url>/', all_menu, name='index'),
]
