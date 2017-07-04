# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from company.models import Company
# from user.models import User
from user.models import UserProfile
from django.contrib.auth.models import User

from .forms import ContactForm, CompanyForm, UserForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Companies</h1>
              <p></p>"""
    return HttpResponse(text)

def view_company(request, id_company):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'entreprise #{0} !".format(id_company)    
    )

def date_actuelle(request):
    return render(request, 'company/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'company/addition.html', locals())

# def accueil(request):
#     """ Afficher tous les articles de notre blog """
#     companies = Company.objects.all() # Nous sélectionnons tous nos articles
#     return render(request, 'company/accueil.html', {'companies': companies})

class CompanyList(ListView):
    model = Company
    context_object_name = "companies"
    template_name = "company/accueil.html"

def lire(request, id):
    company = get_object_or_404(Company, id=id)
    users = company.userprofile_set.all()
    return render(request, 'company/lire.html', {'company':company, 'users':users})

def user(request, id_company, id):
    user = get_object_or_404(UserProfile, id=id)
    return render(request, 'company/user.html', {'user':user})

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        name = form.cleaned_data['name']
        # message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'company/contact.html', locals())

def company(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # form = CompanyForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        name = form.cleaned_data['name']
    #     # Nous pourrions ici envoyer l'e-mail grâce aux données 
    #     # que nous venons de récupérer
    #     envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'company/company.html', locals())

def addUser(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # form = CompanyForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    form = UserForm(request.POST or None)
    if form.is_valid():
        # form.save()
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        comp = Company.objects.get(name=company)
        use = User.objects.create_user(name, 'mathieu@crepes-bretonnes.com', 'sup3rp@ssw0rd')
        pro = UserProfile(user=use, company=comp)
        pro.company = comp
        use.save()

    #     
    # Nous pourrions ici envoyer l'e-mail grâce aux données 
    #     # que nous venons de récupérer
    #     envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'company/addUser.html', locals())

