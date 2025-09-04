from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('album/',views.album,name="album"),
    path('admin/', admin.site.urls),
    path('info/',views.info,name="info"),
    path('preguntas/',views.preguntas,name="preguntas"),
]