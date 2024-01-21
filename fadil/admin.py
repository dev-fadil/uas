from django.contrib import admin

# Register your models here.
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis, ChatID

class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif","banner_satu","banner_dua",)
    prepopulated_fields = {"slug": ("nama",)}

class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk", "gambar","harga","no_whatsup",)
    prepopulated_fields = {"slug": ("nama_produk",)} 

class DataKontak(admin.ModelAdmin):
    list_display = ("nama", "no_whatsup", "email", "subject", "isi")

admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Produk, DataProdukAdmin)
admin.site.register(Slide)
admin.site.register(Kontak, DataKontak)
admin.site.register(Profil)
admin.site.register(Statis)
admin.site.register(ChatID)
