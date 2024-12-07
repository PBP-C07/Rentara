from django.urls import path, include
from .views import *

app_name = 'sewajual'

urlpatterns = [
    path('katalog/', vehicle_list, name='vehicle_list'),
    path('katalog/<uuid:pk>/', full_info, name='full_info'),
    path('vehicles/adm/', admin_vehicle_list, name='admin_vehicle_list'),
    path('vehicles/adm/add/', add_vehicle, name='add_vehicle'),
    path('vehicles/adm/<uuid:pk>/edit/', edit_vehicle, name='edit_vehicle'),
    path('vehicles/adm/<uuid:pk>/delete/', delete_vehicle, name='delete_vehicle'),
    path('bookmarks/', include('bookmark.urls', namespace='bookmark')),
    path('xml/', show_xml, name='show_xml'),
    path('vehicle/json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_product_flutter, name='create_vehicle_flutter'),
]