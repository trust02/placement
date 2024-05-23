from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('student_signup', views.student_signup, name="student_signup"),
    path('company_signup', views.company_signup, name="company_signup"),
    path('admin_signup', views.admin_signup, name="admin_signup"),
    path('companies_login', views.companies_login, name="companies_login"),
    path('student_login',views.student_login, name="student_login"),
    path('admin_login',views.admin_login, name="admin_login"),
    path('student_dashboard', views.student_dashboard, name="student_dashboard"),
    path('job_listing', views.job_listing, name="job_listing"),
    path('profile_management', views.profile_management, name="profile_management"),
    path('company_dashboard', views.company_dashboard, name="company_dashbaord"),
    path('post_attachment', views.post_attachment, name="post_attachment"),
    path('manage_applications', views.manage_applications, name="manage_applications"),
    path('profile_update', views.profile_update, name="profile_update"),
    path("logout", views.logout, name="logout"),
    path('attachment_apply', views.attachment_apply, name="attachment_apply"),
    path('search', views.search, name="search" ),
    path('count', views.count, name="count"),
    path('reply', views.reply, name="reply"),
    path('students_applying',views.students_applying, name="students_applying"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('approved_students', views.approved_students, name="approved_students"),
    path('adpost', views.adpost, name="adpost"),
    
]   
