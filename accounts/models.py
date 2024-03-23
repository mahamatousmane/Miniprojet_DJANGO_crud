from django.db import models

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

class Article(models.Model):
    nom = models.CharField(max_length=64, unique=True, verbose_name= "Nom")
    description = models.TextField(verbose_name= "Description")
    prix = models.IntegerField(default = 1, verbose_name= "Prix")
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, verbose_name= "Categorie")
    
    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        permissions = [
            ('apply_promo_code', 'Peut appliquer des migrations'),
            ('apply_promo', 'Peut appliquer des migrations')
        ]