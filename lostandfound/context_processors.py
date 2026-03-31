from django.conf import settings


def media_url(_request):
    return {"MEDIA_URL": settings.MEDIA_URL}
