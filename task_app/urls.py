from django.urls import path
from task_app import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import forgot_password, CustomPasswordResetConfirmView


urlpatterns = [
    path('home',views.home),
    #path('modelform',views.modelform),
    path('add_customer',views.add_customer),
    path('update/<int:tid>',views.update),
    path('all_customers',views.all_customers),
    path('userprof_update/<int:tid>/', views.userprof_update, name='userprof_update'),
    path('userprof_update/<int:tid>/', views.userprof_update, name='userprof_update'),
    # path('forgot_password/', forgot_password, name='forgot_password'),
    # path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
    # path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)