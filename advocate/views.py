from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .serializers import AdvocateSerializer,CompaniesSerializer
from .models import Advocate,Companies
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class AdvocateView(ListModelMixin,GenericAPIView):
    '''
    This class is used to get the list of all advocates

    only get method is allowed
    '''
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer 
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class AdvocateDetailView(generics.RetrieveAPIView):
    '''
    This class is used to get the details of a particular advocate

    only get method is allowed
    '''
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)



class CompaniesView(generics.RetrieveAPIView):
    '''
    This class is used to get the list of all companies

    only get method is allowed
    '''
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer  

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class CompanyView(ListModelMixin,GenericAPIView):
    '''
    This class is used to get the list of all advocates

    only get method is allowed
    '''
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer   

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)