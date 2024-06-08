from django.shortcuts import redirect
from django.urls import reverse

class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == reverse('some-view'):
            return redirect('another-view')
        return response
    
    