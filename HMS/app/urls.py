from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
  
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
     path('add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),
    
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='delete_doctor'),
    
    path('doctors/<int:pk>/form/', views.doctor_form, name='doctor_form'),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



