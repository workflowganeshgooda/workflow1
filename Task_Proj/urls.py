"""Task_Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from zusers import views
from django.conf import settings
from django.conf.urls.static import static
from task_app import views
from django.contrib.auth import views as auth_views
from task_app.views import send_otp,reset_password
# from task_app.views import forgot_password, reset_password


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('city_master/', include('masters.main_masters.city_master.urls', namespace='city_master')),
    # path('masters/main_masters/broker_master/', include(('masters.main_masters.broker_master.urls', 'broker_master'))),
    
    #  path('grey_purchase_order/', include('grey_purchase_order.urls')),  # Include your app's URLs here
    path('register_user', views.register_user, name='register_user'),
    path('',views.home),
    # path('form',views.form),
    path('task_app/',include('task_app.urls')),
    path('soft_issue/',include('soft_issue.urls')),
    path('check_in/',include('check_in.urls')),
    

    path('update/<int:tid>',views.update),
    path('delete/<int:tid>',views.delete),
    path('userprof_update/<int:tid>/', views.userprof_update, name='userprof_update'),
    
    path('user_profile/<int:uid>',views.user_profile, name='user_profile'),
    path('user_self_prof_update/<int:tid>',views.user_self_prof_update, name='user_self_prof_update'),
    # path('data',views.data),
    path('login_user', views.login_user, name='login'),
    path('login_admin',views.login_admin, name='loginadmin'),
    path('loginpage',views.loginpage),

    path('logout_user', views.logout_user, name='logout'),
    
    path('header',views.header),
    path('active_users',views.active_users),
    path('deacivate_user/<int:tid>',views.deacivate_user),
    path('activate_user/<int:tid>',views.activate_user),
    path('super_users',views.super_users),
    path('dashboard',views.dashboard),
    path('user_data',views.user_data),
    path('add_customer',views.add_customer),
    # path('update/<int:tid>',views.update),
    path('all_customers',views.all_customers),
    path('DebtorsListAPIView/', views.DebtorsListAPIView.as_view(), name='customer-list'),
    # path('forgot_password/', forgot_password, name='forgot_password'),
    # path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('forgot_password/', send_otp, name='forgot_password'),
    path('reset_password/', reset_password, name='reset_password'),

    # path('forgot_password/', forgot_password, name='forgot_password'),

    # Reset password
    # path('reset_password/', reset_password, name='reset_password'),

    # Password reset views provided by Django
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('delete_user/<int:tid>/', views.delete_user, name='delete_user'),
    # path('update_user_permissions/<int:user_id>/', views.update_user_permissions, name='update_user_permissions'),
    path('backup/', views.backup_database, name='backup_database'),
    path('grant_permission/<int:tid>/', views.grant_permission, name='grant_permission'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
