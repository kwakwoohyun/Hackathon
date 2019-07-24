from allauth.account.adapter import DefaultAccountAdapter

class MyAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return request.GET['next']