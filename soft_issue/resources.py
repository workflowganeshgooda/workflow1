from import_export import resources
from .models import SoftwareIssue

class SoftwareIssueResource(resources.ModelResource):
    class Meta:
        model = SoftwareIssue
        fields = ('id','req_by','req_type','approved','rejected','closed','','email', 'desc', 'att', 'status', 'datadeleted','timestamp','req_by_id','approved_timestamp','rejected_timestamp')

# class SoftwareIssueResource(resources.ModelResource):
#     class Meta:
#         model = SoftwareIssue
#         fields = '__all__'

        
# class SoftwareIssueResource(resources.ModelResource):
#     class Meta:
#         model = SoftwareIssue
#         fields = ()

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields = [field.name for field in self.Meta.model._meta.get_fields()]
