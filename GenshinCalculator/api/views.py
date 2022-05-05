from django.shortcuts import render
from django.http.response import JsonResponse

def calculate( request ):
  return JsonResponse( { "message":"OK" } )

