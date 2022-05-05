from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import ArtifactKind, SecondaryStat, Vision, Weapon, WeaponType

def SecondaryStatCalculate( request ):
  # read parameters from get request
  # get name
  name = request.GET.get( "name" )
  return JsonResponse( { "message":"your name is", "name":name } )

def calculate( request ):
  return JsonResponse( { "message":"OK" } )

