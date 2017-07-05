# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
from django.views.generic import ListView

def addUser(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        company = form.cleaned_data['company']
        mail = form.cleaned_data['mail']
        mdp = form.cleaned_data['mdp']
        comp = Company.objects.get(name=company)
        user = User.objects.create_user(username, mail, mdp)
        user.userprofile.company = comp
        user.userprofile.save()
    return render(request, 'company/addUser.html', locals())

class UserList(ListView):
    model = User
    context_object_name = "users"
    template_name = "company/users.html"

def user(request, id):
	user = User.objects.get(userprofile__id=id)
	return render(request, 'company/user.html', {'user':user})