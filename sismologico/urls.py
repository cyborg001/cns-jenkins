

from django.urls import path

from . import views

urlpatterns = [
    path("sismos/", views.sismos, name="sismos"),
    path('sismo/',views.sismo, name='sismo'),

    path('quienes/',views.quienes, name='quienes'),
    path('base_legal',views.base_legal, name='base_legal'),
    path('', views.inicio, name='inicio'),
    path('register/',views.register, name='register'),
    # apis
    path('sismos/sismos_api/',views.sismos_api, name='sismos_api'),
    path('sismo/sismo_api/<int:sismo_id>',views.sismo_api,name='sismo_api'),
    path('uploader/',views.uploader,name='uploader'),
]