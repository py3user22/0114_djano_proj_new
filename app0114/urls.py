from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('menu-items', views.MenuItemView.as_view()),
]
