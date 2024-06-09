class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to execute for each request before the view (and later middleware) is called.
        
        response = self.get_response(request)
        # Code to execute for each response after the view (and earlier middleware) is called.
        return response