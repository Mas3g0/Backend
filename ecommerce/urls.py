import imp
from django.urls import path
from .views import productView
from ecommerce.views import Myviews 

urlpatterns = [
    path("",productView),
    path('about/',Myviews.as_view())
]


