from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from statelist_app.api.views import property_list, property_detail
from statelist_app.api.views import (EdificationListAV, EdificationDetailAV,
                                     CompanyAV, CompanyDetailAV, ComentaryList,
                                     ComentaryDetail, ComentaryCreate, CompanyVS)

#Use viewsets the not havingtwo or more entities
router = DefaultRouter()
router.register('company', CompanyVS, basename='company')

urlpatterns = [
    path('edification/', EdificationListAV.as_view(), name='edification'),
    path('edification/<int:pk>', EdificationDetailAV.as_view(),
         name='edification-detail'),

    path('', include(router.urls)),

    # path('company/', CompanyAV.as_view(), name='company'),
    # path('company/<int:pk>', CompanyDetailAV.as_view(), name='company-detail'),

    path('edification/<int:pk>/comentary-create/',
         ComentaryCreate.as_view(), name='comentary-create'),

    path('edification/<int:pk>/comentary/',
         ComentaryList.as_view(), name='comentary-list'),

    path('edification/comentary/<int:pk>',
         ComentaryDetail.as_view(), name='comentary-detail'),
]
