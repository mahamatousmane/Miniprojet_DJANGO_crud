from django.contrib import admin
from .models import Categorie, Article


@admin.register(Categorie)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Article)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title', 'author', 'quantity']
    fieldsets = [
        ('Informatios article', {'fields': ['nom', 'categorie'] }),
        ('Informations magasin', {'fields': ['description', 'prix']})
    ]
    
    list_display = ('nom', 'categorie', 'prix')
    list_filter = ['nom', 'categorie']
    search_fields = ['nom', 'categorie__name']
    list_per_page = 10
    
    
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book, BookAdmin)
