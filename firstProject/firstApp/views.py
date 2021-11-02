from django.shortcuts import render
from django.http import JsonResponse

def employeeView(request):
    emp = {
    'id': 123,
    'name': 'John',
    'sal': 10000
    }

    return JsonResponse(emp)

# Create your views here.
