from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("club",views.eventpage,name='club'),
    path("sgs",views.sgsevent,name='sgs'),
    path("register/<str:val>",views.register,name='register'),
    path("send/<str:val>",views.send,name='send')
]
