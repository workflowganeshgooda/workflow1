# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BrokerMasterBrokermaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    brokername = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cityname = models.CharField(max_length=255)
    pincode = models.IntegerField()
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pan = models.CharField(max_length=10)
    gstin = models.CharField(max_length=15)
    tel = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    status = models.CharField(max_length=2)
    addedby = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'broker_master_brokermaster'


class CityMasterCitymaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    cityname = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    statecode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'city_master_citymaster'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TaskAppCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TaskAppCompanyinformationTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    comp_name = models.CharField(unique=True, max_length=100)
    gstno = models.CharField(max_length=15)
    pan = models.CharField(max_length=10)
    logo = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    email_id = models.CharField(unique=True, max_length=254)
    contactno = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    ac_type = models.CharField(max_length=100)
    data_addedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'task_app_companyinformation_table'


class TaskAppCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    email = models.CharField(max_length=254)
    dob = models.DateField(blank=True, null=True)
    user_type = models.CharField(max_length=2, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_app_customuser'


class TaskAppCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(TaskAppCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_app_customuser_groups'
        unique_together = (('customuser', 'group'),)


class TaskAppCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(TaskAppCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_app_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class TaskAppDebtors(models.Model):
    id = models.BigAutoField(primary_key=True)
    deb_name = models.CharField(max_length=50)
    deb_gstin = models.CharField(max_length=15)
    deb_pan = models.CharField(max_length=10)
    deb_address = models.CharField(max_length=500)
    deb_city = models.CharField(max_length=50)
    deb_state = models.CharField(max_length=50)
    deb_pincode = models.CharField(max_length=6)
    deb_email = models.CharField(max_length=50)
    deb_mobile = models.CharField(max_length=10)
    deb_telephone = models.CharField(max_length=10)
    deb_remarks = models.CharField(max_length=1500)
    deb_transport = models.CharField(max_length=50)
    deb_contactperson = models.CharField(db_column='deb_contactPerson', max_length=50)  # Field name made lowercase.
    deb_broker = models.CharField(max_length=50)
    active = models.CharField(max_length=2)
    dataaddedby = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'task_app_debtors'


class TaskAppInvoiceTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    bill_to = models.CharField(max_length=100)
    orderno = models.CharField(max_length=100)
    description = models.TextField()
    hsn = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=100)
    qnty = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    gross = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=10, decimal_places=2)
    sgst = models.DecimalField(max_digits=10, decimal_places=2)
    igst = models.DecimalField(max_digits=10, decimal_places=2)
    taxable = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'task_app_invoice_table'
