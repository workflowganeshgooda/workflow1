# views.py
from django.shortcuts import render, redirect
from .models import CheckIn
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Count
from .models import CheckIn

def check_in(request):
    if request.user.is_authenticated:
        # Check if the user has already checked in today
        today = timezone.now().date()
        checked_in_today = CheckIn.objects.filter(user=request.user, check_in_time__date=today).exists()
        
        if checked_in_today:
            # User has already checked in today, so they can only check out
            if request.method == 'POST':
                # Check if the user has already checked out today
                checked_out_today = CheckIn.objects.filter(user=request.user, check_out_selfie__isnull=False, check_in_time__date=today).exists()
                if not checked_out_today:
                    # User has not checked out today, so they can do it now
                    check_out_selfie = request.FILES.get('check_out_selfie')
                    check_in = CheckIn.objects.filter(user=request.user, check_out_selfie__isnull=True).latest('check_in_time')
                    check_in.check_out_selfie = check_out_selfie
                    check_in.save()
                    return redirect('/')  # Redirect to the home page after check-out
                else:
                    # User has already checked out today
                    # You can add a message here to inform the user
                    return redirect('/')  # Redirect to the home page
            else:
                # Render the check-out form template
                return render(request, 'check_in/check_out.html')
        else:
            # User has not checked in today, so they can check in
            if request.method == 'POST':
                location = request.POST.get('location')
                check_in_selfie = request.FILES.get('check_in_selfie')
                check_out_selfie = request.FILES.get('check_out_selfie')
                check_in = CheckIn.objects.create(user=request.user, location=location, check_in_selfie=check_in_selfie, check_out_selfie=check_out_selfie)
                # Perform any additional processing, e.g., save the selfies to disk
                return redirect('/')  # Redirect to the home page after check-in
            else:
                # Render the check-in form template
                return render(request, 'check_in/check_in.html')
    else:
        return redirect('/')

# def check_in(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             user = request.user
#             location = request.POST.get('location')
#             check_in_selfie = request.FILES.get('check_in_selfie')
#             check_out_selfie = request.FILES.get('check_out_selfie')
#             check_in = CheckIn.objects.create(user=user, location=location, check_in_selfie=check_in_selfie, check_out_selfie=check_out_selfie)
#             # Perform any additional processing, e.g., save the selfies to disk
#             return redirect('/')  # Redirect to the home page after check-in
#         return render(request, 'check_in/check_in.html')  # Render the check-in form template
#     else:
#         return redirect('/')




@login_required
def check_in_data(request):
    if request.user.is_authenticated:
        check_ins = CheckIn.objects.all()  # Fetch all check-in records from the database
        return render(request, 'check_in/check_in_data.html', {'check_ins': check_ins})


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import CheckIn

def check_out(request):
    if request.user.is_authenticated:
        # Check if the user has already checked in today
        today = timezone.now().date()
        check_in_entry = CheckIn.objects.filter(user=request.user, check_in_time__date=today).latest('check_in_time')
        
        if request.method == 'POST':
            check_out_selfie = request.FILES.get('check_out_selfie')
            # Update the check-out time and selfie for the latest check-in entry
            check_in_entry.check_out_time = timezone.now()
            check_in_entry.check_out_selfie = check_out_selfie
            check_in_entry.save()
            return redirect('/')  # Redirect to the home page after check-out
        else:
            # Render the check-out form template
            return render(request, 'check_in/check_out.html')
    else:
        return redirect('/')
