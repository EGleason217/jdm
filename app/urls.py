from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin', views.admin),
    # path ('pictureup', views.pictureup),
]