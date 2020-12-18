from django.conf import settings
from django.db import models

#import uuid

# Create your models here.

class Utilisateur(models.Model):
    #id_utilisateur=models.UUIDField(primary_key=True, default=uuid.uuid4)
    login = models.CharField(max_length=100, null=False, blank=False,help_text='Login...')
    password = models.CharField(max_length=100, null=False, blank=False,help_text='Mot de passe...')
    ROLE = (
    ('e','Enseignant'),
    ('a','Apprenant'),
    
    )

    role = models.CharField(max_length=1,choices = ROLE,blank =True,default ='a',
    )

    def __str__(self):
        return f'{self.login}, {self.role}'