from django.test import TestCase
from .models import Categorie
# unittest

class CategorieTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name = "Alimentaire")
        
    def test_is_correct_instance(self):
        self.assertIsInstance(self.categorie, Categorie)
        
    def test_exists(self):
        categorie = Categorie.objects.get(pk = 1)
        self.assertTrue(categorie)