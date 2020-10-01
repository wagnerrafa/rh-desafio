from django.urls import path
from core.views import index, user_form, post_detail
from . import views
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

app_name = 'core'

urlpatterns = [
   path('',index),
   path('user_form/', user_form),
   path('core/company/<uuid:pk>/', views.post_detail, name='post_detail'),
   url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]