from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<str:id_master>', views.editMaster, name="editMaster"),
    path('deleteMaster/<int:id_website>', views.deleteMaster, name="deleteMaster"),
    path('postdataArtikel/<str:id_website>', views.postdataArtikel, name="postdataArtikel"),
    path('website/<int:id_master>', views.daftarWebsite, name="daftarArtikel"),
    path('editwebsite/<int:id_website>', views.editWebsite, name="editWebsite"),
    path('deletewebsite/<int:id_website>', views.deleteWebsite, name="deleteWebsite"),
    path('artikel/<int:id_website>', views.getWebsiteArtikel, name="editWebsite"),
    path('addMaster', views.addMaster, name="addMaster"),
    path('addWebsite', views.addWebsite, name="addWebsite"),
    path('addArtikel', views.addArtikel, name="addWebsite"),
]