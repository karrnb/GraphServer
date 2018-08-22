from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getShortestPath', views.getShortestPath, name='getShortestPath'),
    path('findLongestShortPath', views.findLongestShortPath, name='findLongestShortPath'),
    path('findSparseNet', views.findSparseNet, name='findSparseNet'),
    path('getConnectedComponents', views.connectedComponents , name='getConnectedComponents'),
    # path('ping', views.ping, name='ping'),
]