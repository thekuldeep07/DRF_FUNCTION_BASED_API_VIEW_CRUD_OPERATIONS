from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response  import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stuList = Student.objects.all()
        serialized = StudentSerializer(stuList,many=True)
        return Response(serialized.data)
    
    if request.method == 'POST':
        data = request.data
        stu = StudentSerializer(data=data)
        if(stu.is_valid()):
            stu.save()
            return Response({"msg":'created Successfully'},status = status.HTTP_201_CREATED)
        return Response(stu.errors,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT':
        id = pk
        data = request.data
        stu = Student.objects.get(id = id)
        ser = StudentSerializer(instance=stu , data=data)
        if(ser.is_valid()):
            ser.save()
            return Response({"msg":"updated completely"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='PATCH':
        id = pk
        data = request.data
        stu = Student.objects.get(id = id)
        ser = StudentSerializer(instance=stu , data=data , partial = True)
        if(ser.is_valid()):
            ser.save()
            return Response({"msg":"updated partially"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    if request.method =="DELETE":
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)





