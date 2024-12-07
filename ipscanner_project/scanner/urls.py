from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_ip, name='scan_ip'),  # URL for scan_ip
    path('login/', views.user_login, name='login'),  # Other URLs
    path('scanner/', views.scanner_page, name='scanner_page'),
]
