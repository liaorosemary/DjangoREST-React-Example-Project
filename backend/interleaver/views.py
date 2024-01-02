from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InterleaverSerializer
from .models import Interleaver

class InterleaverView(viewsets.ModelViewSet):
    serializer_class = InterleaverSerializer
    queryset = Interleaver.objects.all()