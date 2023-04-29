
from django.http import JsonResponse
from . models import employee
from .serializers import serializeremployee,useremployee
from django.contrib.auth.models import User
def serializerlist(request):
    emp=employee.objects.all()
    serializer=serializeremployee(emp,many=True)
    data1=serializer.data
    return JsonResponse(data1,safe=False)

def userlist(request):
    emp=User.objects.all()
    print(emp)
    serializer=useremployee(emp,many=True)
    data1=serializer.data
    return JsonResponse(data1,safe=False)