class CorsMiddleware(object):
    def process_exception(self, request, exception):
        return None