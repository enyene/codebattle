from rest_framework import serializers
from .models import Advocate,Company,Links,Companies




class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    links = LinkSerializer()

    class Meta:
        model = Advocate
        
        fields = [
            'name',
            'profile_pic',
            'short_bio',
            'long_bio',
            'advocate_years_experience',
            'company',
            'links'
        ]

class CompaniesSerializer(serializers.ModelSerializer):
    advocates = AdvocateSerializer(many=True)

    class Meta:
        model = Companies
        fields = [
            'name',
            'logo',
            'summary',
            'href',
            'advocates'
        ]
