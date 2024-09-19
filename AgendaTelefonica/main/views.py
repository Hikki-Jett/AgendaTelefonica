from django.shortcuts import render
from .models import Contacts
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token


@csrf_exempt
def createContact(request):
    if request.method == 'POST':
        dataPost = json.loads(request.body)

        contact = Contacts.objects.create(
            name = dataPost['name'],
            lastName = dataPost['lastName'],
            phoneNumber = dataPost['phoneNumber'],
            phoneNumberWork = dataPost['phoneNumberWork'],
            email = dataPost['email']
        )
        return JsonResponse({'Guardado': 'El contacto ha sido guardado correctamente'})
    return JsonResponse({'Error':'El metodo de envio es incorrecto'})

@csrf_exempt
def deleteContact(request):
    if request.method == 'DELETE':
        try:
            dataPost = json.loads(request.body)
            contact = Contacts.objects.get(id = dataPost["id"])
            print(contact)
            contact.delete()
            return JsonResponse({'Eliminado':'El contacto ha sido eliminado'})
        except:
            return JsonResponse({'Error' : 'Esa tarea no se encontró'})
    return JsonResponse({'Error' : 'El metodo de envio es incorrecto'})

@csrf_exempt
def updateContact(request):
    if request.method == 'PUT':
        try:
            dataPost = json.loads(request.body)
            contact = Contacts.objects.get(id = dataPost["id"])
            contact.name = dataPost.get("name", contact.name)
            contact.lastName = dataPost.get("lastName", contact.lastName)
            contact.phoneNumber = dataPost.get("phoneNumber", contact.phoneNumber)
            contact.phoneNumberWork = dataPost.get("phoneNumberWork", contact.phoneNumberWork)
            contact.email = dataPost.get("email", contact.email)
            contact.save()

            return JsonResponse({"Actualizado" : "Contacto Actualizado Correctamente"})
        except:
            return JsonResponse({"Error" : "No se encotro el contacto"})
    return JsonResponse({"Error" : "El metodo de envio es incorrecto"})

def showContacts(request):
    if request.method == 'GET':
        contact = Contacts.objects.all()
        contactList = list(contact.values())

        return JsonResponse(contactList, safe = False)
    return JsonResponse({'Error' : 'El metodo de envio es incorrecto'})

@csrf_exempt
def getTokenCRSF(request):
    token = get_token(request)
    return JsonResponse({"token":token})
# Crear Contacto
# {
#   "name" : "Manuel Alejandro",
#   "lastName" : "Lama Galindo",
#   "phoneNumber" : 9405324692,
#   "phoneNumberWork" : 9456316832,
#   "email" : "prueba_1@gmail.com"
# }

# Eliminar Contacto
# {
#   "id" : 1 
# }