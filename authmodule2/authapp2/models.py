from django.db import models

# Create your models here.
class employee(models.Model):
  ROLE_CHOICES = [
        ('developer', 'Developer (Software Development)'),
        ('designer', 'Designer (UI/UX Design)'),
        ('project_manager', 'Project Manager (Management)'),
        ('qa_engineer', 'QA Engineer (Quality Assurance)'),
        ('devops', 'DevOps (Infrastructure and Automation)'),
        ('hr', 'HR (Human Resources)'),
        ('marketing', 'Marketing (Digital Marketing)'),
        ('sales', 'Sales (Business Development)'),
    ]
  DOMAIN_CHOICES = [
        ('software_development', 'Software Development'),
        ('design', 'UI/UX Design'),
        ('management', 'Project Management'),
        ('qa', 'Quality Assurance'),
        ('infrastructure', 'Infrastructure'),
        ('hr_department', 'Human Resources'),
        ('digital_marketing', 'Digital Marketing'),
        ('business_development', 'Business Development'),
    ]
  name=models.CharField(max_length=50)
  roal=models.CharField(max_length=50,choices=ROLE_CHOICES)
  domain_name=models.CharField(max_length=50,choices=DOMAIN_CHOICES)
  project_name=models.CharField(max_length=200)