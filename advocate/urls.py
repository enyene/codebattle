from django.urls import path,include,re_path
from .views import AdvocateView,AdvocateDetailView,CompaniesView,CompanyView,Home
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('api/advocate/',AdvocateView.as_view(),name='advocate'),
    path('api/advocate/<int:pk>',AdvocateDetailView.as_view(),name='advocate-detail'),
    
    path('api/companies/<int:pk>',CompaniesView.as_view(),name='company'),
    path('api/companies/',CompanyView.as_view(),name='companies'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

