from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('api/menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('secret', views.secret),
    path('api/secret/', views.secret),
]
