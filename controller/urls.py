from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.homepage,name="home"),
    path('viewapplicants',views.viewapplicants,name="viewapplicants"),

]