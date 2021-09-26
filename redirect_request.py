from redirect_response import RedirectResponse
from request import Request


class RedirectRequest:


    def __init__(self, url):
        
        self.url = url
        self._init_request()


    def _init_request(self):

        response = Request(self.url).get()
        self.response = RedirectResponse(response)

    
    def get_response(self):

        return self.response


    def is_redirect(self):

        return self.response.is_redirected()