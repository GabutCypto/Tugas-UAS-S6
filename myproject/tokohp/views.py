from rest_framework import viewsets
from .models import Kategori, HP, Penjualan, MetodePembayaran
from .serializers import KategoriSerializer, HPSerializer, PenjualanSerializer, MetodePembayaranSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class HPViewSet(viewsets.ModelViewSet):
    queryset = HP.objects.all()
    serializer_class = HPSerializer

class MetodePembayaranViewSet(viewsets.ModelViewSet):
    queryset = MetodePembayaran.objects.all()
    serializer_class = MetodePembayaranSerializer

class PenjualanViewSet(viewsets.ModelViewSet):
    queryset = Penjualan.objects.all()
    serializer_class = PenjualanSerializer
