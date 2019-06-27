"""qubeInfraSight URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.urls import path, include
#from rest_framework import routers
#from .views import *
from django.urls import path,include
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'',views.CustomerViewSet)

# router.register(r'customers', CustomerViewSet)
# router.register(r'address', AddressViewSet)
# router.register(r'email', EmailViewSet)
# router.register(r'custcommchannel', CustomerCommChannelViewSet)
# router.register(r'addinfo', CustomerAddInfoViewSet)
# router.register(r'legalinfo', LegalInfoViewSet)
# router.register(r'phone', PhoneViewSet)
# router.register(r'projects', ProjectViewSet)
# router.register(r'projectsattributes', ProjectAttributeViewSet)
#router.register(r'customer', CustomerAggregateViewSet)
# router.register(r'^searchcustomer', customer_list())

# urlpatterns = [
#     path('projectoffice/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
urlpatterns = [

    path('projectoffice/',include(router.urls)),
    path('createcust/',views.createcust,name='createcustomer'),
    #path('updatecust/',views.updatecust,name='Updatecustomer')
]

# http://127.0.0.1:8000/projectoffice/customer
# http://127.0.0.1:8000/projectoffice/customer/2/