from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin', views.admin),
    path('booking',views.booking),
    path('order',views.order),
    # path ('pictureup', views.pictureup),
]