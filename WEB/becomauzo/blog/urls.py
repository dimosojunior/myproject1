from django.urls import path
from .import views

urlpatterns = [

   
    path('', views.home, name="home"),
    
    path('base/', views.base, name="base"),
    path('services/', views.services, name="services"),
    path('add_product/', views.add_product, name="add_product"),
    path('service_detail/<int:pk>/', views.service_detail, name="service_detail"),
  
   
   

 
    
    
 
    
 
]
   
   

 
    
    
 
    
 
