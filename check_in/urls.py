# masters/main_masters/city_master/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
# urls.py
from django.urls import path
from .views import check_in, check_in_data

app_name = 'check_in'  # Add app_name if needed

urlpatterns = [
    path('check_in/', check_in, name='check_in'),
    path('check_in_data/', check_in_data, name='check_in_data'),  # Map the view to a URL pattern
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)