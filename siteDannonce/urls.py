"""siteDannonce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from annonces.views import CategoryViewset,SubcategoryViewset,AnnonceViewset,UserViewset,\
    AdminCategoryViewset,AdminSubcategoryViewset,AdminAnnonceViewset
router = routers.SimpleRouter()
router.register('category',CategoryViewset,basename='category')
router.register('subcategory',SubcategoryViewset,basename='subcategory')
router.register('annonces',AnnonceViewset,basename='annonces')
router.register('admin/category',AdminCategoryViewset,basename='admin-category')
router.register('admin/subcategory',AdminSubcategoryViewset,basename='admin-subcategory')
router.register('admin/annonces',AdminAnnonceViewset,basename='admin-annonces')
router.register('users',UserViewset,basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
