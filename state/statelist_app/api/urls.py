from django.urls import path
# from statelist_app.api.views import property_list, property_detail
from statelist_app.api.views import EdificationListAV, EdificationDetailAV, CompanyAV, CompanyDetailAV


urlpatterns = [
    path('list/', EdificationListAV.as_view(), name='edification'),
    path('<int:pk>', EdificationDetailAV.as_view(), name='edification-detail'),
    path('company/', CompanyAV.as_view(), name='company'),
    path('company/<int:pk>', CompanyDetailAV.as_view(), name='company-detail'),

]
