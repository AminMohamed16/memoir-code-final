from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accueil.urls')),
    path('ListEvenment/', include('List_Evenment.urls'))
]
