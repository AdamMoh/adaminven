from django.urls import path
from main.views import show_main, create_product,show_xml,show_json,show_xml_by_id,show_json_by_id, register, login_user, logout_user, delete_item, increment_item, decrement_item, edit_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('increment/<int:id>', increment_item, name='increment_item'),
    path('decrement/<int:id>', decrement_item, name='decrement_item'),
    path('edit/<int:id>', edit_item, name='edit_item'),
]