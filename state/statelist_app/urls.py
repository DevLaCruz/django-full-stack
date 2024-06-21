from django.urls import path
from statelist_app.views import property_list, property_detail

urlpatterns = [
    path('list/',property_list, name='prop_list'),
    path('<int:id>', property_detail, name='prop_detail'),
]
