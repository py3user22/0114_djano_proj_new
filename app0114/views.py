from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage


def home(request):
    return render(request, '0114_django_demo.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# 0115 adding method
@api_view()
def secret(request):
    return Response({"message":"secret message @011524' @0110"})
