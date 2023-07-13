from django.urls import path
from . import views

#

urlpatterns = [
    path('demo_items', views.DemoItems)
]
