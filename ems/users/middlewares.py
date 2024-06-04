from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse("account_login")
        signup_url = reverse("account_signup")

        if request.path == login_url or request.path == signup_url:
            return self.get_response(request)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(login_url)
        
        return self.get_response(request)
