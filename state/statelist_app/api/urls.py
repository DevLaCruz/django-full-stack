from django.urls import path
# from statelist_app.api.views import property_list, property_detail
from statelist_app.api.views import PropertyListAV, PropertyDetailAV, CompanyAV


urlpatterns = [
    path('list/',PropertyListAV.as_view(), name='prop_list'),
    path('<int:id>', PropertyDetailAV.as_view(), name='prop_detail'),
    path('company/',CompanyAV.as_view(), name='company'),

]
