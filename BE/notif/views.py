from django.db.models import query
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from notif.models import Item


interested_items = []

def home(request):
    context = {
        "interested_items": interested_items
    }
    return render(request, "notif/home.html", context)


def notify_me(item_kw):
    items = Item.objects.filter(category__title=item_kw)
    data = serialize(queryset=items, format="json")
    interested_items.append(data)
    return JsonResponse(data, encoder=DjangoJSONEncoder, safe=False)