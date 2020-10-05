from django.urls import path
from core.views import *
from core import views

app_name = 'core'

urlpatterns = [
   path('',index, name='index'),
   path('colaborador/', colaborador, name="colaborador"),
   path('core/cadastrar/', cadastrar, name='cadastrar'),
   path('core/company/<uuid:pk>/', views.empresa, name='empresa'),

   path('employee_list/', views.EmployeeList.as_view(), name='employee_list'),
   path('new/', views.EmployeeCreate.as_view(), name='employee_new'),
   path('edit/<uuid:pk>/', views.EmployeeUpdate.as_view(), name='employee_edit'),
   path('delete/<uuid:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),

   path('department_list/', views.DepartmentList.as_view(), name='department_list'),
   path('newDepartment/', views.DepartmentCreate.as_view(), name='department_new'),
   path('editDepartment/<uuid:pk>/', views.DepartmentUpdate.as_view(), name='department_edit'),
   path('deleteDepartment/<uuid:pk>/', views.DepartmentDelete.as_view(), name='department_delete'),

   path('company_list/', views.CompanyList.as_view(), name='company_list'),
   path('editcompany/<uuid:pk>/', views.CompanyUpdate.as_view(), name='company_edit'),
<<<<<<< Updated upstream
   path('deletecompany/<uuid:pk>/', views.CompanyDelete.as_view(), name='company_delete'),
  
   url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


=======
   path('deletecompany/<uuid:pk>/', views.CompanyDelete.as_view(), name='company_delete'),  
>>>>>>> Stashed changes
]