from datetime import datetime
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import CustomUser
# from zusers.models import CustomUser
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone
# from masters.main_masters.city_master.models import CityMaster
from .models import AuditLogCustomUser, CustomUser, Debtors
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from rest_framework import generics, renderers
from django.contrib.auth import authenticate, login
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import Group, Permission,User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate
from rest_framework import generics
from .serializers import DebtorsSerializer
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser  
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model 
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
# def login_user(request):
#     if request.method == 'POST':
#         # Get the username and password entered by the user from the HTML form
#         uname = request.POST.get('username')
#         upass = request.POST.get('password')
#          # Retrieve all users from the CustomUser model
#         all_users = CustomUser.objects.all()
#         # Iterate through all users and compare their attributes
#         for user in all_users:
#             print("allusers",user.username)
#             print("uname",uname)
#             print("pass",upass)
#             print(bool(uname==upass))
#             # Compare entered username and password with user's attributes as strings
#             if user.username == uname and user.password == upass:
#                 return redirect('/dashboard')  # Redirect to the dashboard if a match is found

#     return render(request, 'login.html')
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils import timezone
from django.http import HttpResponse
from django.utils import timezone
from .backup import create_backup
import subprocess

from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import random
from django.http import JsonResponse

from django.contrib.auth.models import Permission
@login_required
# def grant_permission(request, tid):
#     user = get_object_or_404(CustomUser, id=tid)
#     all_permissions = Permission.objects.all()

#     if request.method == 'POST':
#         selected_permissions = request.POST.getlist('permissions')
#         current_permissions = set(user.user_permissions.all())

#         for codename in selected_permissions:
#             try:
#                 permission = all_permissions.get(codename=codename)
#                 user.user_permissions.add(permission)
#             except Permission.DoesNotExist:
#                 return JsonResponse({'error': 'Permission not found'}, status=404)

#         for permission in current_permissions:
#             if permission.codename not in selected_permissions:
#                 user.user_permissions.remove(permission)

#         user.save()

#     vrinda_permissions = [permission.codename for permission in user.user_permissions.all()]

#     permissions = {
#         'add_softwareissue_perm': 'add_softwareissue' in vrinda_permissions,
#         'view_softwareissue_perm': 'view_softwareissue' in vrinda_permissions,
#         'change_softwareissue_perm': 'change_softwareissue' in vrinda_permissions,
#         'delete_softwareissue_perm': 'delete_softwareissue' in vrinda_permissions,

#         'add_brokermaster_perm': 'add_brokermaster' in vrinda_permissions,
#         'view_brokermaster_perm': 'view_brokermaster' in vrinda_permissions,
#         'change_brokermaster_perm': 'change_brokermaster' in vrinda_permissions,
#         'delete_brokermaster_perm': 'delete_brokermaster' in vrinda_permissions
#     }
#     logged_in_user_info = {
#         'logged_in_username': request.user.username,
#         'logged_in_email': request.user.email,
#         # Add other relevant information about the logged-in user
#     }
   
#     context = {
#         'user': user,
#         'all_permissions': all_permissions,
#         'vrinda_permissions': vrinda_permissions,
#         **permissions  # Unpack the permissions dictionary
#     }
#     context.update(logged_in_user_info)

#     return render(request, 'permissions.html', context)


def grant_permission(request, tid):
    user = get_object_or_404(CustomUser, id=tid)
    all_permissions = Permission.objects.all()
    vrinda_permissions = [permission.codename for permission in user.user_permissions.all()]
    print(vrinda_permissions)

    if request.method == 'POST':
        selected_permissions = request.POST.getlist('permissions')
        current_permissions = set(user.user_permissions.all())

        for codename in selected_permissions:
            try:
                permission = all_permissions.get(codename=codename)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                return JsonResponse({'error': 'Permission not found'}, status=404)

        for permission in current_permissions:
            if permission.codename not in selected_permissions:
                user.user_permissions.remove(permission)

        user.save()

    context = {
        'user': user,
        'all_permissions': all_permissions,
        'vrinda_permissions': vrinda_permissions,
    }

    return render(request, 'permissions.html', context)

# @login_required
# def update_user_permissions(request, citymaster_id):
#     # Get the CityMaster instance
#     citymaster = get_object_or_404(CityMaster, pk=citymaster_id)
#     print(citymaster)

#     # Check if the user has permission to add CityMaster
#     can_add_citymaster = request.user.has_perm('city_master.add_citymaster')

#     # Check if the user has permission to update CityMaster
#     can_update_citymaster = request.user.has_perm('city_master.change_citymaster')

#     # Check if the user has permission to delete CityMaster
#     can_delete_citymaster = request.user.has_perm('city_master.delete_citymaster')

#     # data['delete_permission'] = request.user.has_perm('city_master.delete_citymaster')

#     context = {
#         'citymaster': citymaster,
#         'can_add_citymaster': can_add_citymaster,
#         'can_update_citymaster': can_update_citymaster,
#         'can_delete_citymaster': can_delete_citymaster,
#     }

#     if request.method == 'POST':
#         # Assuming you have a form to handle permissions, handle the form submission here
#         # Retrieve selected permissions from the form
#         selected_permissions = request.POST.getlist('selected_permissions')

#         # Add the selected permissions to the user's permissions
#         user = request.user  # Get the current user
#         user.permissions.set(selected_permissions)

#         # Redirect to a success page or render the same page with updated permissions

#     return render(request, 'permissions.html', context)
import os

def backup_database(request):
    if request.user.is_authenticated:
        db_settings = settings.DATABASES['default']
        database_name = db_settings['NAME']
        user = db_settings['USER']
        password = db_settings['PASSWORD']

        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        backup_file_name = f'excella_backup_{timestamp}.sql'
        backup_file_path = os.path.join('D:\\ExcellaBackup\\', backup_file_name)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)

        # Use the `mysqldump` command to create a backup
        command = [
            'C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump',  # Correct path to mysqldump
            f'--user={user}',
            f'--password={password}',
            '--databases',
            database_name,
        ]

        try:
            # Capture the backup data to a variable
            backup_data = subprocess.check_output(command)
            
            # Set the response with a Content-Disposition header specifying an absolute file path
            response = HttpResponse(backup_data, content_type='application/sql')
            response['Content-Disposition'] = f'attachment; filename={backup_file_name}; filename*=UTF-8\'\'{backup_file_path}'
            
            # Write the backup data to the file on the D drive
            with open(backup_file_path, 'wb') as backup_file:
                backup_file.write(backup_data)
            
            return response
        except subprocess.CalledProcessError:
            return HttpResponse('Backup failed.', status=500)

    else:
        return redirect('/login_user')


@login_required
# def userprof_update(request, tid):
#     user = get_object_or_404(CustomUser, id=tid)
#     if request.method == 'POST':
#         user.full_name = request.POST.get('full_name')
#         user.first_name = request.POST.get('first_name')
#         user.last_name = request.POST.get('last_name')
#         user.email = request.POST.get('email')
#         user.dob = request.POST.get('dob')
#         user.address1 = request.POST.get('address1')
#         user.address2 = request.POST.get('address2')
#         user.city = request.POST.get('city')
#         user.pincode = request.POST.get('pincode')
#         user.district = request.POST.get('district')
#         user.state = request.POST.get('state')
#         user.country = request.POST.get('country')
#         user.salary = request.POST.get('salary')
#         user.id_proof = request.POST.get('id_proof')
#         user.address_proof = request.POST.get('address_proof')
#         user.bank_ac_no = request.POST.get('bank_ac_no')
#         user.ifsc_code = request.POST.get('ifsc_code')
#         user.designation = request.POST.get('designation')
#         user.department = request.POST.get('department')

#         # Handle profile picture upload
#         if 'att' in request.FILES:
#             att_file = request.FILES['att']
#             user.att.save(att_file.name, att_file)  # Save the file to a permanent location
#             # Set the att field to the URL of the uploaded file
#             # user.att = user.att.url
#         else:
#             # If no file is uploaded, set att to None
#             user.att = None

#         user.save()

#         # Create an audit log for the update
#         previous_data = {
#             'full_name': user.full_name,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'dob': user.dob,
#             'address1': user.address1,
#             'address2': user.address2,
#             'city': user.city,
#             'pincode': user.pincode,
#             'district': user.district,
#             'state': user.state,
#             'country': user.country,
#             'salary': user.salary,
#             'id_proof': user.id_proof,
#             'address_proof': user.address_proof,
#             'bank_ac_no': user.bank_ac_no,
#             'ifsc_code': user.ifsc_code,
#             'designation': user.designation,
#             'department': user.department,
#             'att': user.att.url if user.att else None,
#         }

#         AuditLogCustomUser.objects.create(
#             action='update',
#             model_name='CustomUser',
#             record_id=user.id,
#             user=request.user,
#             timestamp=timezone.now(),
#             username=request.user.username,
#             previous_data=previous_data,
#             new_data=previous_data
#         )

#         return redirect('/active_users')
#     else:
#         context = {'user': user}
#         return render(request, 'userprof_update.html', context)

def userprof_update(request, tid):
    user = get_object_or_404(CustomUser, id=tid)

    if request.method == 'POST':
        att_file = request.FILES.get('att')  
        # Handle profile picture upload
        if att_file:
            if not default_storage.exists(user.att.name) or att_file.name != user.att.name:
                # Save the file to the user's att field
                user.att.save(att_file.name, att_file)
        # Save the file to the user's att field

        # Process other user information
        user.full_name = request.POST.get('full_name')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        user.address1 = request.POST.get('address1')
        user.address2 = request.POST.get('address2')
        user.city = request.POST.get('city')
        user.pincode = request.POST.get('pincode')
        user.district = request.POST.get('district')
        user.state = request.POST.get('state')
        user.country = request.POST.get('country')
        user.salary = request.POST.get('salary')
        user.id_proof = request.POST.get('id_proof')
        user.address_proof = request.POST.get('address_proof')
        user.bank_ac_no = request.POST.get('bank_ac_no')
        user.ifsc_code = request.POST.get('ifsc_code')
        user.designation = request.POST.get('designation')
        user.department = request.POST.get('department')
        user.is_superuser = request.POST.get('is_superuser')
        # is_superuser_value = request.POST.get('is_superuser')
        # user.is_superuser = is_superuser_value == 'on'  # Convert 'on' to True, otherwise False

        
        

        # Save the user object
        user.save()

        # Create an audit log for the update
        previous_data = {
            'full_name': user.full_name,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'dob': user.dob,
            'address1': user.address1,
            'address2': user.address2,
            'city': user.city,
            'pincode': user.pincode,
            'district': user.district,
            'state': user.state,
            'country': user.country,
            'salary': user.salary,
            'id_proof': user.id_proof,
            'address_proof': user.address_proof,
            'bank_ac_no': user.bank_ac_no,
            'ifsc_code': user.ifsc_code,
            'designation': user.designation,
            'department': user.department,
            'is_superuser': user.is_superuser,
            
            'att':user.att,
            'att': user.att.url if user.att else None,
        }

        AuditLogCustomUser.objects.create(
            action='update',
            model_name='CustomUser',
            record_id=user.id,
            user=request.user,
            timestamp=timezone.now(),
            username=request.user.username,
            previous_data=previous_data,
            new_data=previous_data
        )
        
        if request.method == 'POST':
            if 'att' in request.FILES:
                att_file = request.FILES['att']
                custom_url = "prof_pics/"
                modified_filename = att_file.name
                att_with_custom_url = custom_url + modified_filename
                # Update the 'att' field for the user with the uploaded file
                CustomUser.objects.filter(id=tid).update(att=att_with_custom_url)

        # if request.method == 'POST':
        #     if 'att' in request.FILES:
        #         custom_url = "uploads/"
        #         modified_filename = "modified_" + att.name
        #         att_with_custom_url = custom_url + modified_filename
        #         att_file = request.FILES['att']
        #         # Update the 'att' field for the user with the uploaded file
        #         CustomUser.objects.filter(id=tid).update(att=att_with_custom_url)

            return redirect(request.path)
        else:
            content={}
            content['data']=CustomUser.objects.get(id=tid)
        return redirect('/active_users')
    
    else:
        context = {'user': user}
        return render(request, 'userprof_update.html', context)






# @login_required 
# def update_user_permissions(request, user_id):
#     CustomUser = get_user_model()  # Get the custom user model

#     user = get_object_or_404(CustomUser, pk=user_id)  # Use the custom user model

#     if request.method == 'POST':
#         # Get the selected permissions from the form
#         add_permission = request.POST.get('add_permission') == 'on'
#         view_permission = request.POST.get('view_permission') == 'on'
#         update_permission = request.POST.get('update_permission') == 'on'

#         # Define permission codenames
#         add_permission_codename = 'add_permission'
#         view_permission_codename = 'view_permission'
#         update_permission_codename = 'update_permission'

#         # Get content types for CustomUser and Permission models
#         user_content_type = ContentType.objects.get_for_model(CustomUser)  # Use the custom user model
#         permission_content_type = ContentType.objects.get_for_model(CustomUser)

#         # Add or remove permissions based on the form input
#         if add_permission:
#             user.auth_permission.add(
#                 auth_permission.objects.get(
#                     codename=add_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )
#         else:
#             CustomUser.auth_permission.remove(
#                 auth_permission.objects.get(
#                     codename=add_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )

#         if view_permission:
#             user.auth_permission.add(
#                 auth_permission.objects.get(
#                     codename=view_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )
#         else:
#             user.auth_permission.remove(
#                 auth_permission.objects.get(
#                     codename=view_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )

#         if update_permission:
#             user.auth_permission.add(
#                 auth_permission.objects.get(
#                     codename=update_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )
#         else:
#             user.user_permissions.remove(
#                 auth_permission.objects.get(
#                     codename=update_permission_codename,
#                     content_type=permission_content_type
#                 )
#             )

#         messages.success(request, 'Permissions updated successfully.')
#         return redirect('update_user_permissions', user_id=user_id)

#     return render(request, 'update_user_permissions.html', {'user': user})

# 


# def register_user(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         if request.method == 'POST':
#             uname = request.POST['username']
#             upass = request.POST['password2']
#             uemail = request.POST['email']
#             profile_picture = request.POST['profile_picture']

#             # Check if a user with the same username or email already exists
#             if CustomUser.objects.filter(username=uname).exists() or CustomUser.objects.filter(email=uemail).exists():
#                 error_message = "User with this username or email already exists."
#                 f = UserCreationForm()
#                 content = {'form': f, 'error_message': error_message}
#                 return render(request, 'register_user.html', content)

#             hashed_password = make_password(upass)

#             # Create and save the user
#             user = CustomUser(username=uname, email=uemail, password=hashed_password,profile_picture=profile_picture,is_active=1)
#             user.save()

#             # Send registration success email to user
#             subject_user = 'Registration Successful'
#             from_email_user = 'gslucky.2011@gmail.com'  # Update with your email address

#             # Custom HTML content for the user email
#             html_content_user = f'''
#             <html>
#                 <body>
#                     <h1>Hello {uname},</h1>
#                     <h2>You have successfully registered with on WorkFlow.</h2>
#                     <p>contact your admin for account activation</p>
#                     <p>This is an auto-generated email!</p>
#                 </body>
#             </html>
#             '''

#             # Create an EmailMultiAlternatives instance for user email
#             email_message_user = EmailMultiAlternatives(subject_user, '', from_email_user, [uemail])
#             email_message_user.attach_alternative(html_content_user, "text/html")
#             email_message_user.send()

#             # Send registration notification email to admin
#             subject_admin = 'New User Registration'
#             from_email_admin = 'gslucky.2011@gmail.com'  # Update with your email address
#             admin_email = 'ganeshgooda@gmail.com'  # Admin email address

#             # Custom HTML content for the admin email
#             html_content_admin = f'''
#             <html>
#                 <body>
#                     <h1>New user registered:</h1>
#                     <p>Username: {uname}</p>
#                     <p>Email: {uemail}</p>
#                 </body>
#             </html>
#             '''

#             # Create an EmailMultiAlternatives instance for admin email
#             email_message_admin = EmailMultiAlternatives(subject_admin, '', from_email_admin, [admin_email])
#             email_message_admin.attach_alternative(html_content_admin, "text/html")
#             email_message_admin.send()

#             return redirect('/login_user')
#         else:
#             f = UserCreationForm()
#             content = {'form': f}
#             return render(request, 'register_user.html', content)

def register_user(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        if request.method == 'POST':
            uname = request.POST['username']
            upass = request.POST['password2']
            uemail = request.POST['email']
            
          

            # Check if a user with the same username or email already exists
            if CustomUser.objects.filter(username=uname).exists() or CustomUser.objects.filter(email=uemail).exists():
                error_message = "User with this username or email already exists."
                f = UserCreationForm()
                content = {'form': f, 'error_message': error_message}
                return render(request, 'register_user.html', content)

            hashed_password = make_password(upass)

            # Create and save the user with profile picture
            user = CustomUser(username=uname, email=uemail, password=hashed_password,is_active=1)
            user.save()

            # Send registration success email to user
            subject_user = 'Registration Successful'
            from_email_user = 'gslucky.2011@gmail.com'
            to_email_user = uemail

            # Custom HTML content for the user email
            html_content_user = f'''
            <html>
                <body>
                    <h1>Hello {uname},</h1>
                    <h2>You have successfully registered with on WorkFlow.</h2>
                    <p>Contact your admin for account activation.</p>
                    <p>This is an auto-generated email!</p>
                </body>
            </html>
            '''

            # Create an EmailMultiAlternatives instance for user email
            email_message_user = EmailMultiAlternatives(subject_user, '', from_email_user, [to_email_user])
            email_message_user.attach_alternative(html_content_user, "text/html")
            email_message_user.send()

            # Send registration notification email to admin
            subject_admin = 'New User Registration'
            from_email_admin = 'gslucky.2011@gmail.com'
            to_email_admin = 'ganeshgooda@gmail.com'

            # Custom HTML content for the admin email
            html_content_admin = f'''
            <html>
                <body>
                    <h1>New user registered:</h1>
                    <p>Username: {uname}</p>
                    <p>Email: {uemail}</p>
                </body>
            </html>
            '''

            # Create an EmailMultiAlternatives instance for admin email
            email_message_admin = EmailMultiAlternatives(subject_admin, '', from_email_admin, [to_email_admin])
            email_message_admin.attach_alternative(html_content_admin, "text/html")
            email_message_admin.send()

            return redirect('/login_user')
        else:
            f = UserCreationForm()
            content = {'form': f}
            return render(request, 'register_user.html', content)


def loginpage(request):
    return render(request, 'login.html')

#-------FORGOT PASSWORD -----------------------#
CustomUser = get_user_model()



def dashboard(request):
    if request.user.is_authenticated:
        ago20m = timezone.now() - timezone.timedelta(minutes=120)
        notlogged = timezone.now()

        countlogin = CustomUser.objects.filter(last_login__gte=ago20m).count()
        user_loggedin20 = CustomUser.objects.filter(last_login__gte=ago20m)
        
        user_not_logged = CustomUser.objects.filter(last_login__lt=notlogged)
  

        totalusers = CustomUser.objects.count()
        countoffline = totalusers - countlogin
     

        datas = Debtors.objects.all()
        data = {'datas': datas, 'countlogin': countlogin, 'totalusers': totalusers, 'countoffline': countoffline, 'user_loggedin20': user_loggedin20, 'user_not_logged': user_not_logged}
        
        return render(request, 'data.html', data)
    else:
        return redirect('/login_user')  # 


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/dashboard')
            else:
                login(request, user)
                return redirect('/')  # Redirect to user data view for non-admin users
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect to login page on authentication failure
            
    else:
        return render(request, 'login.html')  # Render the login page for GET requests
    
def login_admin(request):
    if request.user.is_superuser:
        messages.error(request, 'Only Admin can login here -- Use CustomUser Login to proceed --')
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            usernam = request.POST['username']
            passwor = request.POST['password']
            user = authenticate(request, username=usernam, password=passwor)
            if user is not None:
                login(request, user)
                messages.error(request, 'Only Admin can login here -- Use CustomUser Login to proceed --')
                return redirect('/login_admin')

            else:
                messages.error(request, 'Invalid Credentials or CustomUser Inactive')
                return redirect('login')
        else:
            logout(request)
            return render(request, 'admin_login.html')
            

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logout successfull")
        return redirect('/login_user')
    else:
        return redirect('/login_user')

@login_required
def deacivate_user(request,tid):
    if request.user.is_authenticated:
        deacivate_user = CustomUser.objects.filter(id=tid)
        deacivate_user.update(is_active=False)
        return redirect ('/active_users')
    else:
        return redirect ('/')
    
def activate_user(request,tid):
    activate_user = CustomUser.objects.filter(id=tid)
    activate_user.update(is_active=True)
    return redirect ('/active_users')

from django.shortcuts import render
# Create a new file context_processors.py in your Django app directory

def device_type(request):
    # Detect device type based on user-agent
    is_desktop = True  # Assume desktop by default (for demonstration)
    if request.META.get('HTTP_USER_AGENT'):
        user_agent = request.META.get('HTTP_USER_AGENT').lower()
        is_desktop = 'mobile' not in user_agent
    
    # Return a dictionary with the variable you want to include in all templates
    return {'isDesktop': is_desktop}

# def home(request):
    # Detect device type based on user-agent
    # is_desktop = True  # Assume desktop by default (for demonstration)
    # if request.META.get('HTTP_USER_AGENT'):
    #     user_agent = request.META.get('HTTP_USER_AGENT').lower()
    #     is_desktop = 'mobile' not in user_agent
    
    # Pass the device type to the template context
    # return render(request, 'home.html', {'isDesktop': is_desktop})
    # return render(request, 'home.html')
# views.py

def home(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    print(user_agent,"ggg")  # Print user agent string to console for debugging
    return render(request, 'home.html')


# def home(request):
#     if request.user.is_authenticated:

#         datas = {}
#         datas['datas']=Debtors.objects.all()
# # city master
#         datas['view_city_master_home'] = request.user.has_perm('city_master.view_citymaster')
#         datas['add_city_master_home'] = request.user.has_perm('city_master.add_citymaster')
#         datas['change_city_master_home'] = request.user.has_perm('city_master.change_citymaster')
#         datas['delete_city_master_home'] = request.user.has_perm('city_master.delete_citymaster')
#     #   Broker master
#         datas['view_broker_master_home'] = request.user.has_perm('broker_master.view_brokermaster')
#         datas['add_broker_master_home'] = request.user.has_perm('broker_master.add_brokermaster')
#         datas['change_broker_master_home'] = request.user.has_perm('brker_master.change_brokermaster')
#         datas['delete_broker_master_home'] = request.user.has_perm('broker_master.delete_brokermaster')
#  #datas['superuser_false'] = CustomUser.objects.filter(is_superuser=False)
#         datas['datas'] = Debtors.objects.filter(dataaddedby='ganesh')
#         #datas['add_permission'] = request.user.has_perm('library.add_Debtors')
#         datas['update_permission'] = request.user.has_perm('library.change_Debtors')
#         datas['users'] = Debtors.objects.values_list('dataaddedby').distinct()
        
#         datas['user_change_permission'] = request.user.has_perm('auth.change_user')
#         #datas['delete_permission'] = request.user.has_perm('library.delete_Debtors')
#         #datas['view_permission'] = request.user.has_perm('library.view_Debtors')
        
#         return render(request,'home.html',datas)
#     else:
#         return render(request,'home.html')

def delete(request,tid):
    delete = Debtors.objects.filter(id=tid)
    delete.delete()
    return redirect('/data')

def data(request):
    if request.user.is_authenticated:
        datas = {}
        user_id = CustomUser.objects.filter(is_superuser=False).filter(is_active=True)
        #print(user_id)
        datas['datas']=[]
        datas['user_id_records'] = []
        for d in user_id:
            datas['user_id_records'].append(str(d.id))
            list_user_data=task_app.myobjects.filter(active='y').filter(dataadded_by=d.id).values_list('dataadded_by','book_name','auth_name','book_price','book_type','publisher','published_on')
            datas['datas'].append(list_user_data)
        print( datas['datas'])
        print(datas['user_id_records'])
        datas['book_type'] = Lib_Man_Sys_Table.myobjects.values_list('book_type').distinct()
        datas['add_permission'] = request.user.has_perm('library.add_lib_man_sys_table')
        datas['update_permission'] = request.user.has_perm('library.change_lib_man_sys_table')
        datas['delete_permission'] = request.user.has_perm('library.delete_lib_man_sys_table')
        datas['view_permission'] = request.user.has_perm('library.view_lib_man_sys_table')
        return render(request,'data.html',datas)
    else:
        return render(request,'login.html')
def data1(request):
    if request.user.is_authenticated:
        datas = {}
        datas['datas']=Debtors.objects.all()
        #datas['add_permission'] = request.user.has_perm('library.add_Debtors')
        datas['update_permission'] = request.user.has_perm('library.change_Debtors')
        datas['users'] = Debtors.objects.values_list('dataaddedby').distinct()
        datas['superuser_false'] = CustomUser.objects.filter(is_superuser=False)
        datas['user_change_permission'] = request.user.has_perm('auth.change_user')
        #datas['delete_permission'] = request.user.has_perm('library.delete_Debtors')
        #datas['view_permission'] = request.user.has_perm('library.view_Debtors')
        ago20m  = timezone.now() - timezone.timedelta(minutes=120)
        #no_login = timezone.now() - timezone.timedelta(minutes=100)
        
        countlogin = CustomUser.objects.filter(last_login__gte=ago20m).count()
        #countoffline = CustomUser.objects.filter(last_login__gte=no_login).count()
        datas = Debtors.objects.all()
        data ={'datas':datas,'countlogin':countlogin,}
        #return render(request,'data.html',data)
        
        totalusers = CustomUser.objects.count()
        print(totalusers)
        countofflince = totalusers-countlogin
        print(countofflince)


        data = {'countlogin':countlogin,'countoffline':countlogin,'datas':datas,'countofflince':countofflince,'totalusers':totalusers}
        return render(request,'data.html',data)
    else:
        return render(request,'login.html')


def user_data(request):
    if request.user.is_authenticated:
        datas = {}        
        #datas['add_permission'] = request.user.has_perm('library.add_Debtors')
        datas['update_permission'] = request.user.has_perm('library.change_Debtors')
        datas['users'] = Debtors.objects.values_list('dataaddedby').distinct()
        datas['superuser_false'] = CustomUser.objects.filter(is_superuser=False)
        datas['user_change_permission'] = request.user.has_perm('auth.change_user')
        #datas['delete_permission'] = request.user.has_perm('library.delete_Debtors')
        #datas['view_permission'] = request.user.has_perm('library.view_Debtors')
        ago20m  = timezone.now() - timezone.timedelta(minutes=120)
        #no_login = timezone.now() - timezone.timedelta(minutes=100)
        countlogin = CustomUser.objects.filter(last_login__gte=ago20m).count()
        #countoffline = CustomUser.objects.filter(last_login__gte=no_login).count()
        datas = Debtors.objects.filter(dataaddedby=request.user.id)
        data ={'datas':datas,'countlogin':countlogin,}
        #return render(request,'data.html',data)
        
        totalusers = CustomUser.objects.count()
        print(totalusers)
        countofflince = totalusers-countlogin
        print(countofflince)


        data = {'countlogin':countlogin,'countoffline':countlogin,'datas':datas,'countofflince':countofflince,'totalusers':totalusers}
        return render(request,'user_data.html',data)
    else:
        return render(request,'login.html')


class DebtorsListAPIView(generics.ListAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer
    renderer_classes = [renderers.JSONRenderer]


def all_customers(request):
    if request.user.is_authenticated:
        # Query all customer records from the Debtors model
        customers = Debtors.objects.all()
        print(customers)
        # Pass the list of customers to the template
        return render(request, 'all_customers.html', {'datas': customers})
      
    else:
        return render(request, 'login.html')
    

def header(request):
    if request.user.is_authenticated:
        data ={}
        data['datas']=Debtors.objects.filter(active='y')
        data['book_type'] = Debtors.objects.values_list('book_type').distinct()
        data['add_permission'] = request.user.has_perm('library.add_Debtors')
        data['update_permission'] = request.user.has_perm('library.change_Debtors')
        data['delete_permission'] = request.user.has_perm('library.delete_Debtors')
        data['view_permission'] = request.user.has_perm('library.view_Debtors')
        data['user_change_permission'] = request.user.has_perm('auth.change_user')
        return render(request,'library/header.html',data)
    else:
        return render(request,'library/header.html')

def active_users(request):
    if request.user.is_authenticated:
        data = {}
        # data['superuser_false'] = CustomUser.objeomcts.all
        
        # data['superuser_false'] = CustomUser.objects.filter(is_superuser=False)
        data['superuser_false'] = CustomUser.objects.all
        data['user_change_permission'] = request.user.has_perm('auth.change_user')
        return render(request,'active_users.html',data)
    else:
        return redirect('/login_user')
    
def delete_user(request,tid):
    delete = CustomUser.objects.filter(id=tid)
    delete.delete()
    return redirect('/active_users')




# def form(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             c_name = request.POST['c_name']
#             c_address = request.POST['c_address']
#             c_email = request.POST['c_email']
#             c_mobile = request.POST['c_mobile']
#             product_id = request.POST['product_id']
#             product_name = request.POST['prod_name']
#             insert_data = Debtors.objects.create(prod_name=product_name,product_id=product_id,c_mobile=c_mobile,c_email=c_email,c_address=c_address,c_name=c_name,dataaddedby=request.user.id)
#             insert_data.save()
#             return redirect('/user_data')
#     else:
#         return redirect('/login_user')
#     return render(request,'form.html')

def add_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            deb_name = request.POST['deb_name']
            deb_gstin = request.POST['deb_gstin']
            deb_pan = request.POST['deb_pan']
            deb_address = request.POST['deb_address']
            deb_city = request.POST['deb_city']
            deb_state = request.POST['deb_state']
            deb_pincode = request.POST['deb_pincode']
            deb_email = request.POST['deb_email']
            deb_mobile = request.POST['deb_mobile']
            deb_telephone = request.POST['deb_telephone']
            deb_remarks = request.POST['deb_remarks']
            deb_transport = request.POST['deb_transport']
            deb_contactPerson = request.POST['deb_contactPerson']
            deb_broker = request.POST['deb_broker']
          
            # Create a new instance and save it to the database
            insert_data = Debtors.objects.create(
                deb_name=deb_name,
                deb_gstin=deb_gstin,
                deb_pan=deb_pan,
                deb_address=deb_address,
                deb_city=deb_city,
                deb_state=deb_state,
                deb_pincode=deb_pincode,
                deb_email=deb_email,
                deb_mobile=deb_mobile,
                deb_telephone=deb_telephone,
                deb_remarks=deb_remarks,
                deb_transport=deb_transport,
                deb_contactPerson=deb_contactPerson,
                deb_broker=deb_broker,
                dataaddedby=request.user.username
            )
            
            return redirect('/all_customers')
    else:
        return redirect('/login_user')
    
    return render(request, 'add_customer.html')
def add_invoice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            deb_name = request.POST['deb_name']
            deb_gstin = request.POST['deb_gstin']
            deb_pan = request.POST['deb_pan']
            deb_address = request.POST['deb_address']
            deb_city = request.POST['deb_city']
            deb_state = request.POST['deb_state']
            deb_pincode = request.POST['deb_pincode']
            deb_email = request.POST['deb_email']
            deb_mobile = request.POST['deb_mobile']
            deb_telephone = request.POST['deb_telephone']
            deb_remarks = request.POST['deb_remarks']
            deb_transport = request.POST['deb_transport']
            deb_contactPerson = request.POST['deb_contactPerson']
            deb_broker = request.POST['deb_broker']
          
            # Create a new instance and save it to the database
            insert_data = Debtors.objects.create(
                deb_name=deb_name,
                deb_gstin=deb_gstin,
                deb_pan=deb_pan,
                deb_address=deb_address,
                deb_city=deb_city,
                deb_state=deb_state,
                deb_pincode=deb_pincode,
                deb_email=deb_email,
                deb_mobile=deb_mobile,
                deb_telephone=deb_telephone,
                deb_remarks=deb_remarks,
                deb_transport=deb_transport,
                deb_contactPerson=deb_contactPerson,
                deb_broker=deb_broker,
                dataaddedby=request.user.username
            )
            
            return redirect('/all_customers')
    else:
        return redirect('/login_user')
    
    return render(request, 'add_customer.html')


def user_profile(request, uid):
    if request.user.is_authenticated:
        contain = {}
        contain['user'] = CustomUser.objects.get(id = uid)
        return render(request, 'user_profile.html', contain)
    else:
        return redirect('/login_user')



def super_users(request):
    if request.user.is_authenticated:
        super_user = CustomUser.objects.filter(is_superuser=True)
        users = {'super_user':super_user}
        return render(request,'super_users.html',users)
    else:
        return redirect('/login_user')

def inactive_users(request):
    if request.user.is_authenticated:
        inactive_users = CustomUser.objects.filter(is_staff=0)
        users = {'inactive_users':inactive_users}
        print(all_users)
        return render(request,'active_users.html',users)


def update(request,tid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            c_name = request.POST['c_name']
            c_address = request.POST['c_address']
            c_email = request.POST['c_email']
            c_mobile = request.POST['c_mobile']
            product_id = request.POST['product_id']
            product_name = request.POST['product_name']
            insert_data = Debtors.objects.filter(id=tid)
            product_id = request.POST['product_id']
            insert_data.update(id=tid,product_name=product_name,product_id=product_id,c_mobile=c_mobile,c_email=c_email,c_name=c_name,c_address=c_address,active='y')
            return redirect ('/data')
        else:
           content = {}
           content['data'] = Debtors.objects.get(id=tid)
           return render(request,'update.html',content)
    else:
        return redirect ('/login_user')
    

def user_self_prof_update(request, tid):
    if request.method == 'POST':
        #username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        insert_data = CustomUser.objects.filter(id=tid)
        insert_data.update(first_name=first_name, last_name=last_name, email=email)
        return redirect('/user_profile/' + str(tid))
    else:
        content = {}
        content['data'] = CustomUser.objects.get(id=tid)
        return render(request, 'user_self_prof_update.html', content)

# def forgot_password(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = CustomUser.objects.get(email=email)
#             except CustomUser.DoesNotExist:
#                 # Handle case where email doesn't exist
#                 return render(request, 'forgot_password.html', {'form': form, 'error_message': 'Email does not exist'})
            
#             # Generate a token for password reset
#             token = default_token_generator.make_token(user)
            
#             # Construct the password reset link
#             reset_link = request.build_absolute_uri(reverse_lazy('password_reset_confirm', kwargs={'uidb64': user.pk, 'token': token}))
            
#             # Send password reset email
#             subject = 'Password Reset Request'
#             message = f'Click the following link to reset your password: {reset_link}'
#             send_mail(subject, message, 'from@example.com', [email])
            
#             return render(request, 'password_reset_sent.html')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'forgot_password.html', {'form': form})

# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'password_reset_confirm.html'
#     success_url = reverse_lazy('login_user')
#     form_class = SetPasswordForm



CustomUser = get_user_model()

def generate_otp():
    # Generate a 6-digit OTP
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            # Generate password reset token and send email with OTP
            token = default_token_generator.make_token(user)
            subject = 'Password Reset OTP'
            from_email = 'your_email@example.com'  # Update with your email address

            # Generate OTP
            otp = generate_otp()

            # Custom HTML content for the email
            html_content = f'''
            <html>
                <body>
                    <h1>Password Reset OTP</h1>
                    <p>Your OTP for password reset is: {otp}</p>
                </body>
            </html>
            '''

            # Send email with OTP
            email_message = EmailMultiAlternatives(subject, '', from_email, [email])
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

            # Store the OTP in session for verification
            request.session['reset_otp'] = otp
            request.session['reset_email'] = email

            return render(request, 'reset_password.html')

    # If it's a GET request or if email doesn't exist, render the forgot password form
    return render(request, 'forgot_password.html')



logger = logging.getLogger(__name__)
def reset_password(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        print(otp_entered)
        new_password = request.POST.get('new_password')
        print(new_password)
        email = request.session.get('reset_email')
        print(email)
        otp_stored = request.session.get('reset_otp')
        print(otp_stored)

        if otp_entered != otp_stored:
            return HttpResponseBadRequest("Invalid OTP. Please try again.")

        try:
            user = CustomUser.objects.get(email=email)
            print(user)
        except CustomUser.DoesNotExist:
            return HttpResponseBadRequest("User does not exist.")

        # Set and save the new password
        user.set_password(new_password)
        user.save()

        # Redirect to login page
        return redirect('login')  # Assuming 'login' is the name of the login page URL pattern

    return render(request, 'reset_password.html')