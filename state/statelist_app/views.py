from django.shortcuts import render
from statelist_app.models import Property
from django.http import JsonResponse

# Create your views here.

def property_list(request):
    state=Property.objects.all()
    data={
        'state':list(state.values())
    }

    return JsonResponse(data)


def property_detail(request, id):
    property=Property.objects.get(pk=id)
    data={
        'address':property.address,
        'country':property.country,
        'image':property.image,
        'description':property.description,
        'active':property.active
    }

    return JsonResponse(data)