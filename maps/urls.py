from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update_marker_coordinates',views.update_marker_coordinates,name='update_marker_coordinates'),
]
