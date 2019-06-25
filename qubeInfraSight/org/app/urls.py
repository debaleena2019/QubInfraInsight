from django.urls import path,include
from rest_framework import routers
from .import views
router=routers.DefaultRouter()
router.register(r'',views.orgViewSet)
#router.register(r'create',views.createOrg)
#router.register(r'add_attribute',views.attributeViewSet)
#router.register(r'comm_attribute',views.commViewSet)
#router.register(r'comm_phone',views.phoneViewSet)
#router.register(r'comm_address',views.addressViewSet)
#router.register(r'comm_email',views.emailViewSet)
#router.register(r'legal_attribute',views.legalViewSet)
#router.register(r'orgaggregate',views.orgAggregateViewSet)
urlpatterns = [

    path('organizations/',include(router.urls)),
    path('createOrg/',views.createorg,name='createOrganisation'),
    path('updateOrg/',views.updateorg,name='UpdateOrganisation')
]
