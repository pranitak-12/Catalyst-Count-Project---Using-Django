from rest_framework import serializers
from catalyst_app.models import company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ['company_id', 'name', 'domain', 'year_founded', 'industry', 'country','locality','country','linkedin_url','current_emp_est','total_emp_est']
