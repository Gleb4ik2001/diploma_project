from django.http import HttpResponseRedirect
from django.urls import reverse

class HandleAttributeErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, AttributeError):
            return HttpResponseRedirect(reverse('login'))
        return None
