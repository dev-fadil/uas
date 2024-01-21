from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('cari', views.cari, name='cari'),
    path('tentang-kami', views.tentang, name='tentang'),
    path('kontak', views.KontakView.as_view(), name='kontak'),
    path('profil', views.profil, name='profil'),
    path('<slug:slug>', views.kategori, name='kategori'),
    path('<slug:kategori_slug>/<slug:slug>', views.singleproduct, name="singleproduct"),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),

]
