from django.conf import settings
from django.http import JsonResponse


def health_endpoint(request):
    response = {
        "debug": settings.DEBUG,
        "status": "ok",
    }
    return JsonResponse(response, status=200)
