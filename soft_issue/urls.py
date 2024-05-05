# masters/main_masters/city_master/urls.py
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .import views

urlpatterns = [
    path('view_soft_issue/',views.view_soft_issue, name='view_soft_issue'),
    # path('city_detail/<int:pk>/', views.city_detail, name='city_detail'),
    path('add_soft_issue/', views.add_soft_issue, name='add_soft_issue'),
    # path('reject_soft_issue/<int:tid>/', views.reject_soft_issue, name='reject_soft_issue'),
    path('reject_soft_issue/<int:tid>/', views.reject_soft_issue, name='reject_soft_issue'),
    path('approve_soft_issue/<int:tid>/', views.approve_soft_issue, name='approve_soft_issue'),
    

    path('deleted_soft_issue/', views.deleted_soft_issue, name='deleted_soft_issue'),
    path('export_soft_issue_to_excel/', views.export_soft_issue_to_excel),
    path('export_soft_issue_pdf/', views.export_soft_issue_pdf),
    path('view_soft_issue_grid/', views.view_soft_issue_grid),
    path('soft_issue_deleted/', views.soft_issue_deleted, name="soft_issue_deleted"),
    path('restore_soft_issue_deleted/<int:tid>/', views.restore_soft_issue_deleted, name='restore_soft_issue_deleted'),
    path('perm_soft_issue_delete/<int:tid>/', views.perm_soft_issue_delete, name='perm_soft_issue_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)