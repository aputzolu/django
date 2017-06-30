# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class User(models.Model):
   name = models.CharField(max_length=100)
   company = models.ForeignKey('Company')

   def __str__(self):
        return self.name