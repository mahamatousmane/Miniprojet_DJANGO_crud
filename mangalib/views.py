from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import datetime
from .models import Article, Categorie
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

def is_visitor(user):
    return user.groups.filter(name = "Visiteur").exists()

# settings.LOGNI_URL : /accounts/login


def index(request):
    context = {
        "books": Article.objects.all()
    }
    
    return render(request,"mangalib/index.html", context)

@user_passes_test(is_visitor)
def show(request, book_id):
    context = {"book": get_object_or_404(Article, pk = book_id)}
    return render(request, "mangalib/show.html", context)    

def add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = ArticleForm()
        
    return render(request,"mangalib/book-form.html", {"form": form})

def edit(request, book_id):
    book =  Article.objects.get(pk = book_id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = book)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = ArticleForm(instance = book)
        
    return render(request,"mangalib/book-form.html", {"form": form})    
 

def remove(request, book_id):
    book =  Article.objects.get(pk = book_id)
    book.delete()

    return redirect("mangalib:index")
 
