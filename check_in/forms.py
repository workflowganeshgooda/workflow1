# from django import forms
# from .models import SoftwareIssue

# class SoftwareIssueForm(forms.ModelForm):
#     class Meta:
#         model = SoftwareIssue
#         fields = ['req_by', 'email', 'desc', 'att']

# class SoftwareIssueFilterForm(forms.Form):
#     req_by = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'style': 'width: 140px;'}))
#     CHOICES = (
#         ('Software related', 'Software related'),
#         ('Hardware related', 'Hardware related'),
#         ('Attendance related', 'Attendance related'),
#     )
#     req_type = forms.ChoiceField(choices=CHOICES, required=False, widget=forms.Select(attrs={'style': 'width: 140px; height:29px;'}))
#     # req_type = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'style': 'width: 140px;'}))
    
#     email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'style': 'width: 140px;'}))
#     desc = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'style': 'width: 140px;'}))
#     att = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'style': 'width: 140px;'}))
   
#     status = forms.BooleanField(required=False)
#     datadeleted = forms.BooleanField(required=False)
#     id = forms.IntegerField(label='Req No.', required=False, widget=forms.TextInput(attrs={'style': 'width: 50px;'}))
