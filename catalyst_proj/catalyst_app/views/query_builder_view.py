from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.serializers import serialize
from django.template import loader
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from catalyst_app.models import company
from catalyst_app.serializers import CompanySerializer
from django.urls import reverse
from django.db import connection,DataError
import os
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        
        template = loader.get_template('data_filter.html')
        context = {
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect('login') 

@api_view(['POST'])
def filter_company_data(request):
    industry = request.data.get('industry', None)
    company_name = request.data.get('company_name', None)
    year_founded = request.data.get('yr_founded', None)
    country = request.data.get('country', None)

    queryset = company.objects.all()

    industry_count = company_name_count = year_founded_count = country_count = 0

    if industry:
        industry_queryset = queryset.filter(industry__icontains=industry)
        industry_count = industry_queryset.count()

    if company_name:
        company_name_queryset = queryset.filter(name__icontains=company_name)
        company_name_count = company_name_queryset.count()

    if year_founded:
        year_founded_queryset = queryset.filter(year_founded=year_founded)
        year_founded_count = year_founded_queryset.count()

    if country:
        country_queryset = queryset.filter(country__icontains=country)
        country_count = country_queryset.count()

    serializer = CompanySerializer(queryset, many=True)

    return Response({
        'companies': serializer.data, 
        'industry_count': industry_count,
        'company_name_count': company_name_count,
        'year_founded_count': year_founded_count,
        'country_count': country_count,
    })