from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from po_module.po_customer import views as v_customer
from po_module.po_address import views as v_address
from po_module.po_comm_channel import views as v_comm_channel
from po_module.po_additional_attribute import views as v_additional_attribute
from po_module.po_email import views as v_email
from po_module.po_legal_info import views as v_legal_info
from po_module.po_phone import views as v_phone
from po_module.po_project import views as v_project
from po_module.po_project_attributes import views as v_project_att

router_customer = routers.DefaultRouter()
router_customer.register('po_customer', v_customer.po_customer_ViewSet)

router_address = routers.DefaultRouter()
router_address.register('po_address', v_address.po_addressieViewSet)

router_comm_channel = routers.DefaultRouter()
router_comm_channel.register('po_comm_chanl', v_comm_channel.po_comm_chanlViewSet)

router_additional_attribute = routers.DefaultRouter()
router_additional_attribute.register('po_additional_att', v_additional_attribute.po_additionalViewSet)

router_email = routers.DefaultRouter()
router_email.register('po_email', v_email.po_emailViewSet)

router_legal_info = routers.DefaultRouter()
router_legal_info.register('po_legal_info', v_legal_info.po_legal_infoViewSet)

router_phone = routers.DefaultRouter()
router_phone.register('po_phone', v_phone.po_phoneViewSet)

router_project = routers.DefaultRouter()
router_project.register('po_project', v_project.po_projectViewSet)

router_project_att = routers.DefaultRouter()
router_project_att.register('po_project_att', v_project_att.po_projectAttViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^po_customer', include(router_customer.urls)),
    url(r'^po_address', include(router_address.urls)),
    url(r'^po_comm_channel', include(router_comm_channel.urls)),
    url(r'^po_additional_attribute', include(router_additional_attribute.urls)),
    url(r'^po_email', include(router_email.urls)),
    url(r'^po_legal_info', include(router_legal_info.urls)),
    url(r'^po_phone', include(router_phone.urls)),
    url(r'^po_project', include(router_project.urls)),
    url(r'^po_project_att', include(router_project_att.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
