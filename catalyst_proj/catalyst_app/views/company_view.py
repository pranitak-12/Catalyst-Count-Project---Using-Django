from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.serializers import serialize
from django.template import loader
from django.db import models
from django.db.models import Count, Q
from catalyst_app.models import company,company_summary,Users
from django.urls import reverse
from django.db import connection,DataError
from datetime import datetime, timedelta ,date
import os
from openpyxl import Workbook
import chardet
import csv,sys
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        company_sum = company_summary.objects.all()
        template = loader.get_template('company.html')
        context = {
            'company_sum' : company_sum,
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect('login') 

def upload_company_data(request):
    if request.method == 'POST':
        myfile = request.FILES['csv_file']
        
        if not myfile.name.endswith('.csv'):
            error = "This is not a CSV file"
            return HttpResponse(error)

        file_data = myfile.read()
        encoding = chardet.detect(file_data)['encoding']
        decoded_file = file_data.decode(encoding)
        reader = csv.DictReader(decoded_file.splitlines())
        user_id = request.session['user_id']
        user_name = request.session['username']
        user_instance = get_object_or_404(Users, id=user_id)
        
        company_data = []
        row_count = 0

        for row in reader:
            company_id = row['company_id'] if row['company_id'] else None
            name = row['name'] if row['name'] else None
            domain = row['domain'] if row['domain'] else None
            year_founded = int(row['year founded']) if row['year founded'] else None
            industry = row['industry'] if row['industry'] else None
            size_range = row['size range'] if row['size range'] else None
            locality = row['locality'] if row['locality'] else None
            country = row['country'] if row['country'] else None
            linkedin_url = row['linkedin url'] if row['linkedin url'] else None
            current_emp_est = int(row['current employee estimate']) if row['current employee estimate'] else None
            total_emp_est = int(row['total employee estimate']) if row['total employee estimate'] else None

            company_instance = company(
                company_id=company_id,
                name=name,
                domain=domain,
                year_founded=year_founded,
                industry=industry,
                size_range=size_range,
                locality=locality,
                country=country,
                linkedin_url=linkedin_url,
                current_emp_est=current_emp_est,
                total_emp_est=total_emp_est,
                userid=user_instance
            )
            company_data.append(company_instance)
            row_count += 1
        with transaction.atomic():
            company.objects.bulk_create(company_data)
            company_summary_instance = company_summary(
                file_name=myfile.name, 
                added_by=user_name,
                total_count=row_count 
            )
            company_summary_instance.save()

    return HttpResponseRedirect('/company')
