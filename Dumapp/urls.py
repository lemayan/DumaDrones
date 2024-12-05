"""
URL configuration for Duma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Dumapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('portfoliodetails/', views.portfoliodetails, name='portfoliodetails'),
    path('servicedetails/', views.servicedetails, name='servicedetails'),
    path('starterpage/', views.starterpage, name='starterpage'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('show_images/', views.show_images, name='show_images'),
    path('edit_image/<int:pk>/', views.edit_image, name='edit_image'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('pay_package/', views.pay_package, name='pay_package'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token')
]
