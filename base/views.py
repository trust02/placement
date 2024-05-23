from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from .models import attachmentPost ,registered, adminsignup, approved
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # for password hashing
from .models import companysignup

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def adpost(request):

    if request.method == 'POST':
      company_name = request.POST['company_name']
      company_description = request.POST['company_description']
      company_email = request.POST['email']
      phone_number = request.POST['phone_number']
      attachement_positions = request.POST['attachment_position']
      physical_address = request.POST['physical_address']
      
      
   
      post = attachmentPost(company_name= company_name, company_description=company_description, company_email=company_email, phone_number= phone_number, attachement_positions=attachement_positions,physical_address=physical_address) 
      post.save()
      return redirect("post_attachment")
    else:
        return render(request, 'post_attachment.html')
    
def approved_students(request):

    student_list = approved.objects.all
    return render(request, "approved_students.html", {'all' : student_list})

def students_applying(request):

    student_list = registered.objects.all
   
    return render(request, 'students_applying.html', {'all' : student_list })
    
def admin_dashboard(request):
    approved_count = approved.objects.count()
    object_count = registered.objects.count()
    
    context = {
      'object_count': object_count,
      'approved_count': approved_count,
    }
    return render(request, 'admin_dashboard.html', context,)

def home(request):
    return render(request, 'home.html')

def student_signup(request):
    if request.method == 'POST':
        last_name = request.POST['lastname']
        first_name = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password = request.POST['password']

        if password1 == password:
            if User.objects.filter(email=email).exists():
             messages.info(request, "Email Taken")
             return redirect('student_signup')
            elif User.objects.filter(username=username).exists():
             messages.info(request, "Username Taken")
             return redirect('student_signup')
            else: 
             user = User.objects.create_user(last_name = last_name, first_name=first_name, username=username,email=email,password=password1)
             user.save();
            return redirect('/') 
        else:
             messages.info(request, "Password not matching..")
    else:
        return render(request, "student_signup.html")

def company_signup(request):
    if request.method == 'POST':
        # Extract and validate user data from the form
        company_name = request.POST['company_name']
        company_category = request.POST['company_category']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password = request.POST['password']
           # Hash the password before saving the user
        hashed_password = make_password(password)
        if password1 == password:
            if companysignup.objects.filter(email=email).exists():
                messages.info(request, "Company email already taken")
                return redirect('company_signup')
            elif companysignup.objects.filter(username=username).exists():
                messages.info(request, "Comoany Username alreday Taken")
                return redirect('company_signup') 
            else:
                
                user = companysignup.objects.create(company_category= company_category, company_name= company_name,username=username,email=email,password=password1)
                user.save();
                return redirect('/')
        else:
            messages.info(request, "Passwords should match")
            return render(request, 'company_signup.html')
    else:
        return render(request, 'company_signup.html')         

def admin_signup(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password = request.POST['password']

        if password1 == password:
            if adminsignup.objects.filter(email=email).exists():
             messages.info(request, "Email Taken")
             return redirect('student_signup')
            elif adminsignup.objects.filter(username=username).exists():
             messages.info(request, "Username Taken")
             return redirect('student_signup')
            else: 
             user = adminsignup.objects.create(last_name = last_name, first_name=first_name, username=username,email=email,password=password1)
             user.save();
            return redirect('/') 
        else:
             messages.info(request, "Password should match")
    else: 
        return render(request, "admin_signup.html")

def student_login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_password = request.POST['password']

        user = auth.authenticate(username = user_email,password=user_password)

        if user is not None:
            auth.login(request, user)
            return redirect("student_dashboard")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("student_login")

    else:
        return render(request,"student_login.html")

def companies_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            # Use filter() to handle potential multiple companies with same email
            company = companysignup.objects.filter(email=email).first()
            if company:
                if company.password == password:
                    # Successful login logic
                    request.session['email'] = email
                    request.session['password'] = password
                    return redirect("company_dashbaord")
                else:
                    messages.info(request, "Invalid password. Please try again.")
            else:
                messages.info(request, "Company not found. Please check your email or sign up if you haven't already.")
            return redirect("companies_login")

        except (KeyError, companysignup.DoesNotExist):
            # Handle potential missing fields or database errors
            messages.info(request, "Invalid login information. Please try again.")
            return redirect("companies_login")
    else:
        return render(request, "company_login.html")

def admin_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            # Use filter() to handle potential multiple companies with same email
            admin = adminsignup.objects.filter(email=email).first()
            if admin:
                if admin.password == password:
                    # Successful login logic
                    request.session['email'] = email
                    request.session['password'] = password
                    return redirect("admin_dashboard")
                else:
                    messages.info(request, "Invalid password. Please try again.")
            else:
                messages.info(request, "Adminstratore not found. Please check your email or sign up if you haven't already.")
            return redirect("admin_login")

        except (KeyError, adminsignup.DoesNotExist):
            # Handle potential missing fields or database errors
            messages.info(request, "Invalid login information. Please try again.")
            return redirect("admin_login")
    else:
        return render(request, 'admin_login.html')

def student_dashboard(request):

    object_count = attachmentPost.objects.count()
    context = {'context' :object_count}
   
    return render(request, 'student_dashboard.html', context)

def job_listing(requst):
    post_list = attachmentPost.objects.all
   
    return render(requst, 'job_listing.html', {'all' : post_list })

def profile_management(request):

    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)

    context ={'user':user}

    return render(request, 'profile_management.html', context)

def company_dashboard(request):
    
    return render(request, 'company_dashboard.html')
  
def post_attachment(request):

    if request.method == 'POST':
      company_name = request.POST['company_name']
      company_description = request.POST['company_description']
      company_email = request.POST['email']
      phone_number = request.POST['phone_number']
      attachement_positions = request.POST['attachment_position']
      physical_address = request.POST['physical_address']
      
      
   
      post = attachmentPost(company_name= company_name, company_description=company_description, company_email=company_email, phone_number= phone_number, attachement_positions=attachement_positions,physical_address=physical_address) 
      post.save()

      return redirect("post_attachment")
    
    else:
        return render(request, 'post_attachment.html')

def logout(request):

    auth.logout(request)
    return redirect("/")

def manage_applications(request):
    return render(request, 'manage_applications.html')

def profile_update(request):
    if request.method == 'POST':
        last_name = request.POST['lastname']
        first_name = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
       
        user = User.objects.filter(email=email).update(last_name=last_name,first_name=first_name,username=username,email=email)
       
        return redirect("profile_update")
    else:
        return render(request, "profile_management.html")

def attachment_apply(request):

    if request.method == "POST":
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        college = request.POST['college']
        course = request.POST['course']
        year = request.POST['year']
        EGD = request.POST['EGD']
        LO = request.POST['LO']
        start = request.POST['start']
        end = request.POST['end']
        company = request.POST['company']
        cmp_email = request.POST['company_email']
       
        if full_name != "":         
            user = registered(full_name=full_name,phone_number=phone_number,email=email,physical_address=address,college_name=college,course_name = course,year_of_study=year,graduation_date=EGD,learning_objectives =LO,start_date=start,end_date=end,company_name=company,company_email=cmp_email)
            user.save();

            subject = "Placement Processes"
            message = "Student is Applying for an attachment check on http://127.0.0.1:8000/"

         # Send email notification (replace with appropriate email sending logic)
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [cmp_email],
            fail_silently=False,
            )
            return redirect('job_listing')
        else:
            messages.info(request, "Passwords should match")
    else:
        return render(request, 'attachment_apply.html')

def search(request):

    query = request.GET.get('search')
    if query:
        company = registered.objects.filter(company_name=query)
    else:
        company = registered.objects.all()
    return render(request, 'manage_applications.html', {'registered': company})

def count(request):
    return render(request, 'student_dashboard.html')
    
def reply (request):

    if request.method == "POST":
        stud_email = request.POST['student_email']
        status = "approved"

        try:
            # Retrieve the registered object based on email
            registered_object = registered.objects.get(email=stud_email)

            # Create a new approved object and copy data from registered
            approved_object = approved(email=stud_email)
            for field in approved_object._meta.get_fields():
                # Skip fields that aren't meant to be copied (like primary keys or timestamps)
                if not field.editable or field.primary_key:
                    continue
                value = getattr(registered_object, field.name)
                setattr(approved_object, field.name, value)

                # Ensure the field name matches exactly and is editable
                if field.name == 'attachment_status' and field.editable:
                    approved_object.attachment_status = status

            # Save the copied data with the updated status
            approved_object.save()

            # Send email notification upon successful data copy (optional)
            subject = "Placement Processes"
            message = "Check your platform you have been approved for an Attachment"
            send_mail(
                subject, message, settings.EMAIL_HOST_USER, [stud_email], fail_silently=False
            )
        except registered.DoesNotExist:
            # Handle case where registered object is not found (optional)
            pass
    return render(request, 'manage_applications.html',)