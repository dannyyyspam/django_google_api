from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('route', view.route, name="route"),
    path('map', view.map, name="map"),
]
