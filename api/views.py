from django.shortcuts import render
from api.serializer import EmpSerial
from rest_framework import viewsets
from api.models import Employees
from rest_framework.views import Response


# class EmpView(viewsets.ModelViewSet):
#     serializer_class = EmpSerial
#     queryset = Employees.objects.all()
#
#     def post(self,request, *args, **kwargs):
#         return Response


class EmpView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        qs = Employees.objects.all()
        serialize = EmpSerial(qs, many=True)
        return Response(data=serialize.data)

    def create(self, request, *args, **kwargs):
        serialize = EmpSerial(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = Employees.objects.get(id=id)
        serialize = EmpSerial(qs, many=False)
        return Response(data=serialize.data)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = Employees.objects.get(id=id)
        serialize = EmpSerial(data=request.data, instance=qs)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(serialize.errors)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        Employees.objects.filter(id=id).delete()
        return Response(data='deleted')
