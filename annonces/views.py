from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from annonces.models import Category,Subcategory,Annonce,ATO
from authentification.models import User
from annonces.serializers import CategorySerializer,SubcategorySerializer,AnnonceDetailSerializer,\
    AnnonceListSerializer,AtoSerializer,UserSerializer,AdminSubcategorySerializer,\
    AdminCategoryListSerializer,AdminAnnonceSerializer

# Create your views here.
class AdminCategoryViewset(ModelViewSet):
    serializer_class = AdminCategoryListSerializer

    def get_queryset(self):
        return Category.objects.all()



class AdminSubcategoryViewset(ModelViewSet):
    serializer_class = AdminSubcategorySerializer

    def get_queryset(self):
        return Subcategory.objects.all()

class AdminAnnonceViewset(ModelViewSet):
    serializer_class = AdminAnnonceSerializer

    def get_queryset(self):
        return Annonce.objects.all()
class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class SubcategoryViewset(ReadOnlyModelViewSet):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        return Subcategory.objects.all()

class AnnonceViewset(ReadOnlyModelViewSet):
    serializer_class = AnnonceListSerializer
    detail_serializer_class = AnnonceDetailSerializer

    def get_queryset(self):
        return  Annonce.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' :
            return  self.detail_serializer_class
        return super().get_serializer_class()

class UserViewset(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
