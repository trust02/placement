from django.db import models

# Create your models here.
class attachmentPost(models.Model):
    company_name = models.CharField(null=True)
    company_description = models.CharField(null=True)
    company_email = models.EmailField(primary_key=True,null=False)
    phone_number = models.CharField(null=True)
    attachement_positions = models.CharField(null=True)
    physical_address = models.CharField(null=True)
    date = models.DateField(null=True)

class companysignup(models.Model):
    company_name = models.CharField(null= True)
    company_category= models.CharField(null=True)
    username= models.CharField(null=True)
    email =models.CharField(primary_key = True, null=False)
    password = models.CharField(null=True)

class registered(models.Model):
    full_name = models.CharField(null=True)
    phone_number = models.CharField(null =True)
    email = models.EmailField(primary_key=True, null=False)
    physical_address =models.CharField(null = True)
    college_name = models.CharField(null=True)
    course_name = models.CharField(null= True)
    year_of_study = models.CharField(null=True)
    graduation_date= models.CharField(null=True)
    learning_objectives = models.CharField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    company_name = models.CharField(null=True)
    company_email = models.EmailField(null=True)
    attachment_status = models.CharField(null= True)

class adminsignup(models.Model):
    last_name = models.CharField(null= True)
    first_name= models.CharField(null=True)
    username= models.CharField(null=True)
    email =models.CharField(primary_key = True, null=False)
    password = models.CharField(null=True)

class approved(models.Model):
    full_name = models.CharField(null=True)
    phone_number = models.CharField(null =True)
    email = models.EmailField(null=False)
    physical_address =models.CharField(null = True)
    college_name = models.CharField(null=True)
    course_name = models.CharField(null= True)
    year_of_study = models.CharField(null=True)
    graduation_date= models.CharField(null=True)
    learning_objectives = models.CharField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    company_name = models.CharField(null=True)
    company_email = models.EmailField(null=True)
    attachment_status = models.CharField(null= True, editable=True)
    
