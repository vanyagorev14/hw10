from polls.models import Log


class LogMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response


    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/admin/'):
            Log.objects.create(path=request.path, method=request.method)
