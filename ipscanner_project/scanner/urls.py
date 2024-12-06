from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Login page
    path('scanner/', views.scanner_page, name='scanner_page'),  # Scanner page (where the form is)
   
]
