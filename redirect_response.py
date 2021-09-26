from request import Request


class RedirectResponse:


    def __init__(self, response):
        
        self.response = response

        self.is_redirect = False
        self.history_count = 0
        self.history = []

        self._init_response()


    def _init_response(self):
        
        if not self.response.history:
            return False

        self.is_redirect = True
        self.history = self.response.history
        self.history_count = len(self.history)
        self.redirect_location = self.history[self.history_count - 1]
        


    def is_redirected(self):

        return self.is_redirect


    def get_redirect_location(self):

        return self.redirect_location

    
    def get_redirect_url(self):

        if not self.is_redirect:
            return False

        headers = self.redirect_location.headers

        if 'location' not in headers:
            return False

        return headers['location']


    def get_redirect_status_code(self):

        if not self.is_redirect:
            return False

        headers = self.redirect_location.headers

        if 'location' not in headers:
            return False

        url = headers['location']
        response = Request(url).head()
        
        return response.status_code