from tkinter import Canvas
from django.shortcuts import render, get_object_or_404, redirect
import io
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SoftwareIssue
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import Permission, ContentType
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from .models import AuditLogSoftwareIssue
from django.core.mail import send_mail
from django.conf import settings
from .models import SoftwareIssue
from task_app.models import CustomUser  # Import your SoftwareIssue model
from soft_issue.models import SoftwareIssue
from .forms import SoftwareIssueForm  # You would create a form for adding/editing City records
from django.db.models import Q
import tablib
from .forms import SoftwareIssueFilterForm
from django.http import HttpResponse
# from import_export.formats import XLSX
from .resources import SoftwareIssueResource

# def view_city(request):
#     cities = SoftwareIssue.objects.all()
#     return render(request, 'masters/main_masters/city_master/view_city.html', {'cities': cities})


def export_soft_issue_pdf(request):
    form = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data

    # Retrieve all cities initially
    cities = SoftwareIssue.objects.all()
    permission_content_type = ContentType.objects.get_for_model(Permission)

    # Filter the queryset based on form data
    if form.is_valid():
        cityname = form.cleaned_data['cityname']
        pincode = form.cleaned_data['pincode']
        state = form.cleaned_data['state']
        district = form.cleaned_data['district']
        statecode = form.cleaned_data['statecode']
        country = form.cleaned_data['country']

        if cityname:
            cities = cities.filter(cityname__icontains=cityname)

        if pincode:
            cities = cities.filter(pincode__icontains=pincode)

        if state:
            cities = cities.filter(state__icontains=state)

        if district:
            cities = cities.filter(district__icontains=district)

        if statecode:
            cities = cities.filter(statecode__icontains=statecode)

        if country:
            cities = cities.filter(country__icontains=country)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="city_data.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Define your PDF content here, for example, create a table
    data = [['City Name', 'Pincode', 'State', 'District', 'State Code', 'Country']]
    data.extend([[city.cityname, city.pincode, city.state, city.district, city.statecode, city.country] for city in cities])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
        ('GRID', (0, 0), (-1, -1), 0.5, (0.5, 0.5, 0.5)),
    ]))

    elements.append(table)
    doc.build(elements)

    return response

def soft_issue_deleted(request):
    if request.user.is_authenticated:
     return render(request, 'library/master_data_deleted.html')

def export_soft_issue_to_excel(request):
    form = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data

    # Retrieve all issues initially
    issues = SoftwareIssue.objects.filter(status=1, datadeleted=0)

    # Filter the queryset based on form data
    if form.is_valid():
        req_by = form.cleaned_data.get('req_by')
        req_type = form.cleaned_data.get('req_type')
        email = form.cleaned_data.get('email')
        desc = form.cleaned_data.get('desc')
        att = form.cleaned_data.get('att')
        id = form.cleaned_data.get('id')
        file1 = form.cleaned_data.get('file1')

        # Apply filters
        if id:
            issues = issues.filter(id__icontains=id)
        if req_by:
            issues = issues.filter(req_by__icontains=req_by)
        if req_type:
            issues = issues.filter(req_type__icontains=req_type)
        if email:
            issues = issues.filter(email__icontains=email)
        if desc:
            issues = issues.filter(desc__icontains=desc)
        if att:
            issues = issues.filter(att__icontains=att)
        if file1:
            issues = issues.filter(file1__icontains=file1)

    # Create an export resource instance with XLSX format
    issue_resource = SoftwareIssueResource()

    # Export filtered data to XLSX
    dataset = issue_resource.export(queryset=issues)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="software_issues.xlsx"'

    return response



# def view_city(request):
#     form = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data

#     # Retrieve all cities initially
#     cities = SoftwareIssue.objects.filter(status=1,datadeleted=0)
#     perm_list = request.user.user_permissions.all().values_list('codename', flat=True)
#     print(perm_list)

    
#     # Filter the queryset based on form data
#     if form.is_valid():
#         cityname = form.cleaned_data['cityname']
#         pincode = form.cleaned_data['pincode']
#         state = form.cleaned_data['state']
#         district = form.cleaned_data['district']
#         statecode = form.cleaned_data['statecode']
#         country = form.cleaned_data['country']
#         if cityname:
#             cities = cities.filter(cityname__icontains=cityname)

#         if pincode:
#             cities = cities.filter(pincode__icontains=pincode)

#         if state:
#             cities = cities.filter(state__icontains=state)

#         if district:
#             cities = cities.filter(district__icontains=district)

#         if statecode:
#             cities = cities.filter(statecode__icontains=statecode)
        
#         if country:
#             cities = cities.filter(country__icontains=country)  
          

#     # Pass the filtered queryset to the template
#     return render(request, 'masters/main_masters/city_master/view_city.html', {'cities': cities, 'form': form})

from django.contrib.auth.models import User
def view_soft_issue(request):
    if request.user.is_authenticated:
        data = {}
        data['form'] = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data
        if request.user.is_superuser:
            data['issues'] = SoftwareIssue.objects.filter(status=1, datadeleted=0)
        else:
            data['issues'] = SoftwareIssue.objects.filter(status=1, datadeleted=0, req_by_id=request.user.id)

        # Retrieve approved timestamps for each issue and format if not None
        for issue in data['issues']:
            if issue.approved and issue.approved_timestamp:
                issue.approved_timestamp = issue.approved_timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Convert to string format

        # Sort by ID in descending order
        data['issues'] = data['issues'].order_by('-id')
        print(data)
        # Check user permissions
        data['add_soft_issue'] = request.user.has_perm('soft_issue.add_softwareissue')
        data['view_soft_issue'] = request.user.has_perm('soft_issue.view_softwareissue')
        data['change_soft_issue'] = request.user.has_perm('soft_issue.change_softwareissue')
        data['delete_soft_issue'] = request.user.has_perm('soft_issue.delete_softwareissue')

        # Filter the queryset based on form data
        if data['form'].is_valid():
            req_by = data['form'].cleaned_data.get('req_by')
            req_type = data['form'].cleaned_data.get('req_type')
            email = data['form'].cleaned_data.get('email')
            desc = data['form'].cleaned_data.get('desc')
            att = data['form'].cleaned_data.get('att')
            id = data['form'].cleaned_data.get('id')
            file1 = data['form'].cleaned_data.get('file1')

            # Apply filters
            if id:
                data['issues'] = data['issues'].filter(id__icontains=id)
            if req_by:
                data['issues'] = data['issues'].filter(req_by__icontains=req_by)
            if req_type:
                data['issues'] = data['issues'].filter(req_type__icontains=req_type)
            if email:
                data['issues'] = data['issues'].filter(email__icontains=email)
            if desc:
                data['issues'] = data['issues'].filter(desc__icontains=desc)
            if att:
                data['issues'] = data['issues'].filter(att__icontains=att)
            if file1:
                data['issues'] = data['issues'].filter(file1__icontains=file1)

        return render(request, 'masters/main_masters/software_issue/view_issues.html', data)
    else:
        return redirect('/login_user')



# def view_soft_issue(request):
#     if request.user.is_authenticated:
#         data = {}
#         data['form'] = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data
#         data['issues'] = SoftwareIssue.objects.filter(status=True, datadeleted=False)
      
#         # Filter the queryset based on form data
#         if data['form'].is_valid():
#             req_by = data['form'].cleaned_data.get('req_by')
#             email = data['form'].cleaned_data.get('email')
#             desc = data['form'].cleaned_data.get('desc')
#             att = data['form'].cleaned_data.get('att')
#             status = data['form'].cleaned_data.get('status')
#             datadeleted = data['form'].cleaned_data.get('datadeleted')
            
#             if req_by:
#                 data['issues'] = data['issues'].filter(req_by__icontains=req_by)
            
#             if email:
#                 data['issues'] = data['issues'].filter(email__icontains=email)
            
#             if desc:
#                 data['issues'] = data['issues'].filter(desc__icontains=desc)
            
#             # You can filter based on other fields in a similar manner
            
#         return render(request, 'masters/main_masters/software_issue/view_issues.html', data)
#     else:
#         return redirect('/login_user')



# 
# 
def deleted_soft_issue(request):
    form = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data

    # Retrieve all cities initially
    cities = SoftwareIssue.objects.filter(status=0,datadeleted=1)

    # Filter the queryset based on form data
    if form.is_valid():
        cityname = form.cleaned_data['cityname']
        pincode = form.cleaned_data['pincode']
        state = form.cleaned_data['state']
        district = form.cleaned_data['district']
        statecode = form.cleaned_data['statecode']
        country = form.cleaned_data['country']
        if cityname:
            cities = cities.filter(cityname__icontains=cityname)

        if pincode:
            cities = cities.filter(pincode__icontains=pincode)

        if state:
            cities = cities.filter(state__icontains=state)

        if district:
            cities = cities.filter(district__icontains=district)

        if statecode:
            cities = cities.filter(statecode__icontains=statecode)
        
        if country:
            cities = cities.filter(country__icontains=country)    

    # Pass the filtered queryset to the template
    return render(request, 'masters/main_masters/city_master/deleted_city.html', {'cities': cities, 'form': form})

from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import SoftwareIssueFilterForm
from .models import SoftwareIssue

def view_soft_issue_grid(request):
    form = SoftwareIssueFilterForm(request.GET)  # Bind the form to GET data

    # Initialize the queryset with all SoftwareIssue objects
    if request.user.is_superuser:
        all_issues = SoftwareIssue.objects.filter(status=1, datadeleted=0)
    else:
        all_issues = SoftwareIssue.objects.filter(status=1, datadeleted=0, req_by_id=request.user.id)

    # Pagination
    page = request.GET.get('page', 1)  # Default to page 1
    items_per_page = 1000  # Define the number of items per page

    paginator = Paginator(all_issues, items_per_page)
    issues = paginator.get_page(page)

    # Filter the queryset based on form data if the form is valid
    if form.is_valid():
        req_by = form.cleaned_data.get('req_by')
        req_type = form.cleaned_data.get('req_type')
        email = form.cleaned_data.get('email')
        desc = form.cleaned_data.get('desc')
        att = form.cleaned_data.get('att')
        id = form.cleaned_data.get('id')
        file1 = form.cleaned_data.get('file1')

        # Create a dictionary to map form fields to model fields
        filter_params = {
            'id__icontains': id,
            'req_by__icontains': req_by,
            'req_type__icontains': req_type,
            'email__icontains': email,
            'desc__icontains': desc,
            'att__icontains': att,
            'file1__icontains': file1,
        }

        # Use a loop to apply filters dynamically
        for field, value in filter_params.items():
            if value:
                issues = issues.filter(**{field: value})

    # Pass the filtered queryset and pagination information to the template
    return render(request, 'masters/main_masters/software_issue/view_city_grid.html', {'issues': issues, 'form': form})

# def add_city(request):
#     if request.method == 'POST':
#         form = SoftwareIssueForm(request.POST)
#         if form.is_valid():
#             city = form.save()
#             return redirect('/masters/main_masters/city_master/view_city', pk=city.pk)
#     else:
#         form = SoftwareIssueForm()
#     return render(request, 'masters/main_masters/city_master/add_city.html', {'form': form})

# def city_update(request, tid):
#    if request.user.is_authenticated:
#         if request.method == 'POST':
#             cityname = request.POST['cityname']
#             pincode = request.POST['pincode']
#             district = request.POST['district']
#             state = request.POST['state']
#             country = request.POST['country']
#             statecode = request.POST['statecode']
#             insert_data = SoftwareIssue.objects.filter(id=tid)
#             insert_data.update(id=tid,cityname=cityname,pincode=pincode,state=state,country=country,statecode=statecode)
#             return redirect ('/masters/main_masters/city_master/view_city')
#         else:
#            content = {}
#            content['data'] = SoftwareIssue.objects.get(id=tid)
#            return render(request,'masters/main_masters/city_master/city_update.html',content)
#    else:
#         return redirect ('/masters/main_masters/city_master/view_city')

# def soft_issue_update(request, tid):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             # Retrieve the existing city record
#             city = SoftwareIssue.objects.get(id=tid)
            
#             # Get the updated values from the form
#             cityname = request.POST['cityname']
#             pincode = request.POST['pincode']
#             district = request.POST['district']
#             state = request.POST['state']
#             country = request.POST['country']
#             statecode = request.POST['statecode']

#             # Log the "update" action with username, previous data, and new data
#             AuditLogSoftwareIssue.objects.create(
#                 action='update',
#                 model_name='SoftwareIssue',
#                 record_id=tid,
#                 user=request.user,
#                 username=request.user.username,
#                 previous_data=f'City Name: {city.cityname}, Pincode: {city.pincode}, District: {city.district}',
#                 new_data=f'City Name: {cityname}, Pincode: {pincode}, District: {district}'
#             )

#             # Update the city record
#             city.cityname = cityname
#             city.pincode = pincode
#             city.district = district
#             city.state = state
#             city.country = country
#             city.statecode = statecode
#             city.save()

#             return redirect('/masters/main_masters/city_master/view_city')
#         else:
#             content = {}
#             content['data'] = SoftwareIssue.objects.get(id=tid)
#             return render(request, 'masters/main_masters/city_master/city_update.html', content)
#     else:
#         return redirect('/masters/main_masters/city_master/view_city')# 
# 
# 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def add_soft_issue(request):
    if request.method == 'POST':
        req_by = request.POST.get('req_by')
        req_by_id = request.user.id
        print(req_by_id)

        req_type = request.POST.get('req_type')
        
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        att = request.FILES.get('att')  # Use request.FILES to get the uploaded file
        file1 = request.FILES.get('file1')  # Use request.FILES to get the uploaded file

        # Check if required fields are present
        if req_by and email and desc:
            # Create a new SoftwareIssue instance
            new_issue = SoftwareIssue(req_by=req_by, email=email, desc=desc,req_type=req_type,req_by_id=request.user.id)
            
            # Check if attachments are provided and save them
            if att:
                new_issue.att = att
            if file1:
                new_issue.file1 = file1
            
            # Save the instance
            new_issue.save()

            # Get the ID of the newly created issue
            new_issue_id = new_issue.id

            # Determine if the user is a superuser
            # if request.user.is_superuser:
            admin_email = CustomUser.objects.filter(is_superuser=True).first().email
            # else:
            #     admin_email = 'admin@example.com'  # Default admin email

            # Send email to admin
            send_mail(
                f'New {req_type} Request Added',  # Corrected formatting to include req_type
                f'Dear Admin,\n\n'
                f'A new {req_type} request has been added by {req_by} ({email}).\n\n'
                f'Details: {desc}\n\n'
                f'Request ID: {new_issue_id}\n\n'
                f'Please login to the portal for details.\n\n'
                f'Thank you!',
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
                fail_silently=False,
            )

            # Send email copy to user
            send_mail(
                f'New {req_type} Request Added',  # Subject includes req_type
                f'Your {req_type} request has been successfully added.\n\n'
                f'Details: {desc}\n\n'
                f'Request ID: {new_issue_id}\n\n'
                f'Thank you!',
                settings.DEFAULT_FROM_EMAIL,
                [email],  # Send to the user's email address
                fail_silently=False,
            )

            # Optionally, you can redirect to a success page or render a success message
            return redirect('/soft_issue/view_soft_issue/')
        else:
            # Handle case where required fields are missing
            return HttpResponse("Missing required fields")

    # If the request method is not POST, render the form page
    return render(request, 'masters/main_masters/software_issue/add_issue.html')



# def add_soft_issue(request):
#     if request.method == 'POST':
#         req_by = request.POST.get('req_by')
#         req_by_id = request.user.id
#         print(req_by_id)

#         req_type = request.POST.get('req_type')
        
#         email = request.POST.get('email')
#         desc = request.POST.get('desc')
#         att = request.FILES.get('att')  # Use request.FILES to get the uploaded file
#         file1 = request.FILES.get('file1')  # Use request.FILES to get the uploaded file

#         # Check if required fields are present
#         if req_by and email and desc:
#             # Create a new SoftwareIssue instance
#             new_issue = SoftwareIssue(req_by=req_by, email=email, desc=desc,req_type=req_type,req_by_id=request.user.id)
            
#             # Check if attachments are provided and save them
#             if att:
#                 new_issue.att = att
#             if file1:
#                 new_issue.file1 = file1
            
#             # Save the instance
#             new_issue.save()

#             # Optionally, you can redirect to a success page or render a success message
#             return redirect('/soft_issue/view_soft_issue/')
#         else:
#             # Handle case where required fields are missing
#             return HttpResponse("Missing required fields")

#     # If the request method is not POST, render the form page
#     return render(request, 'masters/main_masters/software_issue/add_issue.html')




# def temp_city_delete(request,tid):
#     temp_delete = SoftwareIssue.objects.filter(id=tid)
#     temp_delete.update(status=0,datadeleted=1)
#     return redirect('/masters/main_masters/city_master/view_city')

def reject_soft_issue(request, tid):
    if request.user.is_superuser:
        issue = SoftwareIssue.objects.get(id=tid)
        issue.rejected = True
        issue.rejected_timestamp = timezone.now()
        issue.save()
        # Redirect to the view issue page or wherever appropriate
        return redirect('view_soft_issue')
    else:
        # Handle unauthorized access
        return redirect('view_soft_issue')
    
# def reject_soft_issue(request, tid):
#     # Get the SoftwareIssue instance to reject
#     software_issue = get_object_or_404(SoftwareIssue, id=tid)
#     rejected = SoftwareIssue.objects.filter(rejected=1)
  
  
#     # Update the rejected field to True
#     software_issue.rejected = True

#     # Save the changes
#     software_issue.save()

#     # Assuming you want to create an audit log entry as well
#     # Create an audit log entry for the "reject" action
#     AuditLogSoftwareIssue.objects.create(
#         action='reject',
#         model_name='SoftwareIssue',
#         record_id=software_issue.pk,
#         user=request.user,
#         username=request.user.username,
#         previous_data=f'Requested by: {software_issue.req_by}, Description: {software_issue.desc}',
#     )

#     # Redirect to the view page or any other appropriate page
#     return redirect('/soft_issue/view_soft_issue/')


# def approve_soft_issue(request, tid):
#     # Get the SoftwareIssue instance to reject
#     software_issue = get_object_or_404(SoftwareIssue, id=tid)
#     # rejected = SoftwareIssue.objects.filter(rejected=1)
#     # print(rejected)

#     # Update the field to True
#     software_issue.approved = True

#     # Save the changes
#     software_issue.save()

#     # Assuming you want to create an audit log entry as well
#     # Create an audit log entry for the "reject" action
#     AuditLogSoftwareIssue.objects.create(
#         action='approve',
#         model_name='SoftwareIssue',
#         record_id=software_issue.pk,
#         user=request.user,
#         username=request.user.username,
#         previous_data=f'Requested by: {software_issue.req_by}, Description: {software_issue.desc}',
#     )

#     # Redirect to the view page or any other appropriate page
#     return redirect('/soft_issue/view_soft_issue/')
# 
# 
def approve_soft_issue(request, tid):
    if request.user.is_superuser:
        issue = SoftwareIssue.objects.get(id=tid)
        issue.approved = True
        issue.approved_timestamp = timezone.now()
        issue.save()
        # Redirect to the view issue page or wherever appropriate
        return redirect('view_soft_issue')
    else:
        # Handle unauthorized access
        return redirect('view_soft_issue')
    
def restore_soft_issue_deleted(request, tid):
        temp_delete = SoftwareIssue.objects.filter(id=tid)
        temp_delete.update(status=1,datadeleted=0)
        if temp_delete.exists():
            # Create an audit log entry for the "delete" action before updating the record
            city = temp_delete.first()

            # Get the previous data for the audit log
            previous_data = f'City Name: {city.cityname}, Pincode: {city.pincode}, District: {city.district}'
            # Create the audit log entry
            AuditLogSoftwareIssue.objects.create(
              
                action='restore',
                model_name='SoftwareIssue',
                record_id=city.pk,
                user=request.user,  # Assuming you're using Django's authentication system
                username=request.user.username,
                previous_data=previous_data,
            )
        return redirect('/masters/main_masters/city_master/view_city')
# def restore_city_deleted(request,tid):
#     temp_delete = SoftwareIssue.objects.filter(id=tid)
#     temp_delete.update(status=1,datadeleted=0)
#     return redirect('/masters/main_masters/city_master/deleted_city')

def perm_soft_issue_delete(request,tid):
    temp_delete = SoftwareIssue.objects.filter(id=tid)
    temp_delete.delete()
    return redirect('/masters/main_masters/city_master/view_city')