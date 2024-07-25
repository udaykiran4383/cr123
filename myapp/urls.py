# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/google-login/', views.google_login, name='google_login'),
    path('api/districts/<str:state_name>/', views.GetDistrictsView.as_view(), name='get_districts'),
    path('api/colleges/<str:state_name>/<str:district_name>/', views.GetCollegesView.as_view(), name='get_colleges'),
     path('api/schools/<str:state_name>/<str:district_name>/', views.GetSchoolsView.as_view(), name='get_schools'),
    path('api/submit-form/', views.SubmitFormView.as_view(), name='submit_form'),
]
