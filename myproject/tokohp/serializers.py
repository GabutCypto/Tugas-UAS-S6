from rest_framework import serializers
from .models import Kategori, HP, Penjualan, MetodePembayaran

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class HPSerializer(serializers.ModelSerializer):
    class Meta:
        model = HP
        fields = '__all__'

class MetodePembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodePembayaran
        fields = '__all__'

class PenjualanSerializer(serializers.ModelSerializer):
    total_harga = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Penjualan
        fields = '__all__'

    def create(self, validated_data):
        hp = validated_data.get('hp')
        jumlah = validated_data.get('jumlah')
        total_harga = hp.harga * jumlah
        validated_data['total_harga'] = total_harga
        
        # Reduce stock
        if hp.stok < jumlah:
            raise serializers.ValidationError("Stok tidak mencukupi")
        hp.stok -= jumlah
        hp.save()

        return super().create(validated_data)
