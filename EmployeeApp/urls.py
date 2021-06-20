from django.conf.urls import url
from EmployeeApp import views
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^department$',views.departmentApi),
    #url(r'^$',views.departmentApi,name='departmentApi'),
    #path('',views.departmentApi,name='department/'),

    url(r'^department/([0-9]+)$',views.departmentApi),
    #path('',views.departmentApi,name='department/'),

    url(r'^employee$',views.employeeApi),
    #url(r'^$',views.employeeApi,name='employeeApi'),
    #path('',views.employeeApi,name='employee/'),

    url(r'^employee/([0-9]+)$',views.employeeApi),
    #path('',views.employeeApi,name='employee/'),

    url(r'^Employee/SaveFile$', views.SaveFile)
    #path('',views.SaveFile,name='Employee/SaveFile/'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)