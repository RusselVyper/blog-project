from django.conf import settings


def default_context(request):
    context_data = {
        "media_url": settings.MEDIA_URL,
        "static_url":settings.STATIC_URL,
    }
    return context_data