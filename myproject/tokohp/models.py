from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Kategori(models.Model):
    nama = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nama

class HP(models.Model):
    nama = models.CharField(max_length=100)
    spesifikasi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey('Kategori', on_delete=models.SET_NULL, null=True, related_name='hps')
    stok = models.PositiveIntegerField(default=0)  # Field untuk stok HP

    def __str__(self):
        return self.nama

from django.db import models

class MetodePembayaran(models.Model):
    nama_metode = models.CharField(max_length=50)
    deskripsi = models.TextField(blank=True, null=True)  # Deskripsi nomor rekening

    def __str__(self):
        return self.nama_metode


    def __str__(self):
        return self.nama_metode

class Penjualan(models.Model):
    hp = models.ForeignKey(HP, on_delete=models.CASCADE, related_name='penjualan')
    tanggal = models.DateField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    metode_pembayaran = models.ForeignKey(MetodePembayaran, on_delete=models.SET_NULL, null=True, related_name='penjualan')

    def __str__(self):
        return f"Penjualan {self.hp.nama} - {self.tanggal}"

    def save(self, *args, **kwargs):
        # Check if there's enough stock
        if self.hp.stok < self.jumlah:
            raise ValueError("Stok tidak mencukupi")
        
        # Calculate total_harga
        self.total_harga = self.hp.harga * self.jumlah
        
        super().save(*args, **kwargs)

@receiver(post_save, sender=Penjualan)
def update_stock(sender, instance, **kwargs):
    instance.hp.stok -= instance.jumlah
    instance.hp.save()
