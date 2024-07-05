from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KategoriViewSet, HPViewSet, PenjualanViewSet, MetodePembayaranViewSet

router = DefaultRouter()
router.register(r'kategori', KategoriViewSet)
router.register(r'hp', HPViewSet)
router.register(r'penjualan', PenjualanViewSet)
router.register(r'metode-pembayaran', MetodePembayaranViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
