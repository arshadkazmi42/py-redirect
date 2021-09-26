from redirect_request import RedirectRequest


class Redirect:
    
    def __init__(self, url):

        self.url = url
        self.redirect_request = RedirectRequest(self.url)


    def get_redirect_request(self):

        return self.redirect_request