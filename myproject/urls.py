"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bukus import views

urlpatterns = [
    path('', views.home, name='index'),
    path('buku', views.index, name='buku'),
    path('buku/testmodel_data', views.TestModelListJson, name="testmodel_list_json"),
    path('buku/create', views.insert, name='buku-create'),
    path('buku/edit/<str:id>', views.edit),
    path('buku/update/<str:id>', views.update),
    path('buku/delete/<str:id>', views.destroy),
]
