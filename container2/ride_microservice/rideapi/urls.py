from django.urls import path
from rideapi import views

urlpatterns = [
    path('api/v1/db/read', views.readDb, name='read'),
    path('api/v1/db/write', views.writeDb, name='write'),
    path('api/v1/rides', views.createRide, name='createRide'),
    path('api/v1/rides/<int:rideId>', views.aboutRides, name='aboutRides'),
    path('api/v1/db/clear', views.clearDb, name='clear'),
]
