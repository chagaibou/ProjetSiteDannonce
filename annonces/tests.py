from django.test import TestCase
from django.urls import reverse_lazy, reverse
from rest_framework.test import  APITestCase
from annonces.models import Category,Subcategory,Annonce,ATO
from authentification.models import User
# Create your tests here.



class TestAnnonce(APITestCase):
    url = reverse_lazy('category-list')

    def test_create(self):
        # Nous vérifions qu’aucune catégorie n'existe avant de tenter d’en créer une
        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'type': 'Nouvelle catégorie'})
        # Vérifions que le status code est bien en erreur et nous empêche de créer une catégorie
        self.assertEqual(response.status_code, 405)
        # Enfin, vérifions qu'aucune nouvelle catégorie n’a été créée malgré le status code 405
        self.assertFalse(Category.objects.exists())

