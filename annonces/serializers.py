from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from annonces.models import Category,Subcategory,Annonce,ATO
from authentification.models import User


class AdminAnnonceSerializer(ModelSerializer):
    class Meta:
        model = Annonce
        fields =['typeDeTransaction','ville','secteur','etat','titreAnnonce',
                 'description','prix','photo','annonceUser','subcategories','dateAnnonce',]
    def validate_prix(self,value):
        if value < 1:
            raise serializers.ValidationError('le prix doit être superieur à 0')

class AnnonceListSerializer(ModelSerializer):
    class Meta:
        model = Annonce
        fields =['typeDeTransaction','description','titreAnnonce','annonceUser','dateAnnonce',]


class AnnonceDetailSerializer(ModelSerializer):
    class Meta:
        model = Annonce
        fields =['typeDeTransaction','ville','secteur','etat','titreAnnonce',
                 'description','prix','photo','annonceUser','subcategories','dateAnnonce',]
    def validate_prix(self,value):
        if value < 1:
            return serializers.ValidationError('le prix doit être superieur à 0')

class AtoSerializer(ModelSerializer):
    class Meta:
        model = ATO
        fields = ['model','marque',]

class AdminSubcategorySerializer(ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['id','type','categories']



class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id','type','categories']

class AdminCategoryListSerializer(ModelSerializer):
    subcategories = SubcategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','type','subcategories']

    def validate_type(self, value):
        if Category.objects.filter(type=value).exists():
            raise serializers.ValidationError('Cette cattegorie existe déjà')

class CategorySerializer(ModelSerializer):
    subcategories = SubcategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','type','subcategories']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','password','telephone']


