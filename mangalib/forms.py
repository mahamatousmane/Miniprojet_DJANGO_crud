from django import forms
from .models import Article, Categorie


class ArticleForm(forms.ModelForm):
    categorie = forms.ModelChoiceField(queryset= Categorie.objects.all(), label="Categorie")
    
    class Meta:
        model = Article
        fields = ['nom', 'categorie', 'description', 'prix']
        labels = {'nom': 'Nom', 'description': 'Description'}
        
    def clean_quantity(self):
        prix = self.cleaned_data['prix']
        
        if prix <= 0 or prix > 100:
            raise forms.ValidationError("Le prix de l'article doit etre comprise entre 1 et 100")
        
        return prix
