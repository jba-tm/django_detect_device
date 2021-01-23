from django.views.generic import RedirectView


class RedirectAppView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.iOS:
            self.url = 'https://apps.apple.com/app/id1542383210'
        elif self.request.Android:
            self.url = 'https://play.google.com/store/apps/details?id=com.ElementApp.Element'
        return super().get_redirect_url(*args, **kwargs)


