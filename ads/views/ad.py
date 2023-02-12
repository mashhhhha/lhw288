import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad

@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):

    def get(self, request):
        response = []
        for ad in Ad.objects.all():
            response.append(
                {"id": ad.id,
                 "name": ad.name,
                 "author": ad.author,
                 "price": ad.price})
        return JsonResponse(response, safe=False)

    def post(self, request, **kwargs):
        data = json.loads(request.body)
        ad = Ad.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            description=data["description"],
            is_published=data["is_published"],
            address=data["address"]

        )
