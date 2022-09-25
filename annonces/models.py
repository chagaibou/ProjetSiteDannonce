from django.db import models
from authentification.models import User
from django.conf import settings
# Create your models here.



class Category(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Subcategory(models.Model):
    type = models.CharField(max_length=200)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='subcategories')

    def __str__(self):
        return self.type


class Annonce(models.Model):
    subcategories = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name='annonces')
    VENTE = 'VENTE'
    DEMANDE = 'DEMANDE'

    TRANSACTION_CHOICES = (
        (VENTE,'vente'),
        (DEMANDE,'Demande')
    )

    NEUF = 'NEUF'
    TRESBON = 'TRESBON'
    BON = 'BON'
    ENDOMMAGE = 'ENDOMMAGE'

    ETAT_CHOICES = (
        (NEUF,'Neuf'),
        (TRESBON,'Très bon'),
        (BON,'Bon'),
        (ENDOMMAGE,'Endommagé'),
    )

    typeDeTransaction = models.CharField(max_length=200,choices=TRANSACTION_CHOICES,default=VENTE)
    ville = models.CharField(max_length=200)
    secteur = models.CharField(max_length=200)
    etat = models.CharField(max_length=200,choices=ETAT_CHOICES)
    titreAnnonce = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    prix = models.DecimalField(max_digits=20,decimal_places=2,blank=True)
    photo = models.ImageField()
    annonceUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='annonces')
    dateAnnonce = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titreAnnonce
class ATO(Annonce):
    model = models.CharField(max_length=200)
    marque = models.CharField(max_length=200)




