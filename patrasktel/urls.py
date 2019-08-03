from django.urls import path
from . import views
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
urlpatterns = [

]
urlpatterns = [
    path('', views.index, name='index'),
    path('routes/', views.route, name='routes'),
    path('announcements/', views.announcement, name='announcements'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tickets/', views.tickets, name='tickets'),
]
handler404 = 'patrasktel.views.handler404'
handler500 = 'patrasktel.views.handler500'
