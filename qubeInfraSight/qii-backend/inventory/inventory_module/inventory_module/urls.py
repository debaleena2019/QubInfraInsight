
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from inventory_module.material_master import views as v_mat_master
from inventory_module.material_unit import views as v_mat_unit
from inventory_module.construction_spec import views as v_const_spec
from inventory_module.construction_spec_mat import views as v_const_spec_mat

router_material_master=routers.DefaultRouter()
router_material_master.register('material_master', v_mat_master.mat_master_ViewSet)

router_material_unit=routers.DefaultRouter()
router_material_unit.register('material_unit', v_mat_unit.mat_unit_ViewSet)

router_const_spec=routers.DefaultRouter()
router_const_spec.register('construction_spec', v_const_spec.const_spec_ViewSet)

router_const_spec_mat=routers.DefaultRouter()
router_const_spec_mat.register('construction_spec_mat', v_const_spec_mat.const_spec_mat_ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^material_master', include(router_material_master.urls)),
    url(r'^material_unit', include(router_material_unit.urls)),
    url(r'^construction_spec', include(router_const_spec.urls)),
    url(r'^construction_spec_mat', include(router_const_spec_mat.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
