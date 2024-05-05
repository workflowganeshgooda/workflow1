from datetime import datetime
from email.policy import default
from django.conf import settings
from django.db import models
from task_app.manager import CustomManager
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# class Task_Table(models.Model):
#     cust_name = models.CharField(max_length=50)
#     cust_gstin = models.CharField(max_length=15)
#     cust_address = models.CharField(max_length=50)
#     cust_email = models.EmailField(max_length=50)
#     cust_mobile = models.CharField(max_length=50)
#     cust_transport =   models.CharField(max_length=50)
#     product_id = models.CharField(max_length=50)
#     product_name = models.CharField(max_length=50)
#     active = models.CharField(max_length=2,default='y')
#     dataaddedby = models.CharField(max_length=50)


class Debtors(models.Model):
    deb_name = models.CharField(max_length=50)
    deb_gstin = models.CharField(max_length=15)
    deb_pan = models.CharField(max_length=10)
    deb_address = models.CharField(max_length=500)
    deb_city = models.CharField(max_length=50)
    deb_state = models.CharField(max_length=50)
    deb_pincode = models.CharField(max_length=6)    
    deb_email = models.EmailField(max_length=50)
    deb_mobile = models.CharField(max_length=10)
    deb_telephone = models.CharField(max_length=10)
    deb_remarks = models.CharField(max_length=1500)   
    deb_transport = models.CharField(max_length=50)
    deb_contactPerson = models.CharField(max_length=50)
    deb_broker = models.CharField(max_length=50)    
    active = models.CharField(max_length=2,default='y')
    dataaddedby = models.CharField(max_length=50)

    #custom_object = models.manager()
   # myobjects = CustomManager()
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models




# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=False)  # Add your custom fields here
#     dob = models.DateField(null=True, blank=True)
#     user_type = models.CharField(null=True, blank=True, max_length=2)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
#     permissions = models.ManyToManyField(Permission, blank=True)

    # Add any additional custom fields you need

 
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(null=True, blank=True, max_length=2)
    # pic = models.ImageField(upload_to='media/uploads/', null=True, blank=True)  # Use 'pic' consistently
    # pic = models.ImageField(upload_to='media/uploads/')
    att = models.ImageField(upload_to='prof_pics/')
    
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    id_proof = models.CharField(max_length=50)
    address_proof = models.CharField(max_length=50)
    bank_ac_no = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    # Override the save method to handle the profile picture
    def save(self, *args, **kwargs):
        if self.att:
            # Clear the profile picture field to prevent it from being saved to the directory
            self.att = None
        super().save(*args, **kwargs)

    # Define the many-to-many relationship with permissions
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users',
    )

    def __str__(self):
        return self.username 

class AuditLogCustomUser(models.Model):
    ACTION_CHOICES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('restore', 'Restore'),  # Add the "restore" action
    )

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=255)
    record_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=255)  # Field for username
    previous_data = models.TextField(blank=True, null=True)  # Field for previous data
    new_data = models.TextField(blank=True, null=True)  # Field for new data

    def __str__(self):
        return f'{self.action} on {self.model_name} (ID: {self.record_id}) by {self.user} at {self.timestamp}'


