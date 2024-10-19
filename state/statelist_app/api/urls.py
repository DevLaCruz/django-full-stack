from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from statelist_app.api.views import property_list, property_detail
from statelist_app.api.views import (EdificationAV, EdificationDetailAV,
                                     CompanyAV, CompanyDetailAV, ComentaryList,
                                     ComentaryDetail, ComentaryCreate, CompanyVS,
                                     UserComentary, EdificationList)

# Use viewsets the not havingtwo or more entities
router = DefaultRouter()
router.register('company', CompanyVS, basename='company')

urlpatterns = [
    path('edification/', EdificationAV.as_view(), name='edification'),
    path('edification/list/',
         EdificationList.as_view(), name='edification-list'),
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

    #     path('edification/comentary/<str:username>',
    #          UserComentary.as_view(), name='user-comentary-detail'),

    path('edification/comentary/',
         UserComentary.as_view(), name='user-comentary-detail'),



]
