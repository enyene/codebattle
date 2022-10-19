from django.urls import path,include
from .views import AdvocateView,AdvocateDetailView,CompaniesView,CompanyView


urlpatterns = [
    path('api', include('rest_framework.urls')),
    path('api/advocate',AdvocateView.as_view(),name='advocate'),
    path('api/advocate/<int:pk>',AdvocateDetailView.as_view(),name='advocate-detail'),
    
    path('api/companies/<int:pk>',CompaniesView.as_view(),name='company'),
    path('api/companies/',CompanyView.as_view(),name='companies'),
]