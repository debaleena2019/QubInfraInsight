
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from .add_additional_address import views as v_additional
from .add_legal_address import views as v_legal
from .add_org import views as v_org
from .org_address import views as v_org_address
from .org_comm_channel import views as v_org_comm_channel
from .org_email import views as v_email
from .org_phn import views as v_phone

router_addorg=routers.DefaultRouter()
router_addorg.register('addorg', v_org.organizationViewSet)

router_additional=routers.DefaultRouter()
router_additional.register('add_additional_address', v_additional.additionalViewSet)

router_legal=routers.DefaultRouter()
router_legal.register('add_legal_address', v_legal.legalViewSet)

router_org_add=routers.DefaultRouter()
router_org_add.register('org_address', v_org_address.orgaddressViewSet)

router_org_comm_channel=routers.DefaultRouter()
router_org_comm_channel.register('org_comm_channel', v_org_comm_channel.commchannelViewSet)

router_email=routers.DefaultRouter()
router_email.register('org_email', v_email.emailViewSet)

router_phone=routers.DefaultRouter()
router_phone.register('org_phn', v_phone.phoneViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^addorg/', include(router_addorg.urls)),
    url(r'^add_additional_address/', include(router_additional.urls)),
    url(r'^add_legal_address/', include(router_legal.urls)),
    url(r'^org_address/', include(router_org_add.urls)),
    url(r'^org_comm_channel/', include(router_org_comm_channel.urls)),
    url(r'^org_email/', include(router_email.urls)),
    url(r'^org_phone/', include(router_phone.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
