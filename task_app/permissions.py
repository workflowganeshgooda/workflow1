from django.contrib.auth.models import Permission

# Create a permission for adding CityMaster instances
add_citymaster_permission, created = Permission.objects.get_or_create(
    codename='add_citymaster',
    name='Can add CityMaster',
)

# Create a permission for updating CityMaster instances
update_citymaster_permission, created = Permission.objects.get_or_create(
    codename='update_citymaster',
    name='Can update CityMaster',
)

# Create a permission for deleting CityMaster instances
delete_citymaster_permission, created = Permission.objects.get_or_create(
    codename='delete_citymaster',
    name='Can delete CityMaster',
)
