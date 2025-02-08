from . import views
from django.urls import path

urlpatterns = [
    path("",views.all_chai,name="all_chai"),
    path("<int:chai_id>/",views.chai_detail,name="chai_detail"),
    path('cstore/',views.chai_store,name='chai_store'),
] 