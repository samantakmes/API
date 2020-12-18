from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):


    # request utilisateurs
    utilisateurs = Utilisateur.objects.filter(role='a')
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_utilisateurs = ["<li>{}</li>".format(utilisateur.login) for utilisateur in utilisateurs]
    message = """<ul>{}</ul>""".format("\n".join(formatted_utilisateurs))
    return HttpResponse(message)
    #return HttpResponse("Bonjour monde!")


def detail(request,nom, pwd):
    
    utilisateur = Utilisateur.objects.get(login=nom, password=pwd)
    message = "Le nom est {}. son role est  {} et son mot de passe est {}".format(utilisateur.login ,utilisateur.role, utilisateur.password)
    return HttpResponse(message)
    return JsonResponse({'resp': response})

@csrf_exempt 
def details(request):
    login = request.POST['login']
    pwd = request.POST['pwd']

    try:
        user = Utilisateur.objects.get(login=login, password=pwd)
    except Utilisateur.DoesNotExist:
        user = None
    
    if not user:
        return JsonResponse({'statut': 'NONOK'})
    return JsonResponse({'login': user.login, 'pwd': user.password, 'role': user.role, 'statut': 'OK'})