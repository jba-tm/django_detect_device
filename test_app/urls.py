from django.urls import path
from .views import RedirectAppView, IosView, AndroidView, PcView

urlpatterns = [
    path('', RedirectAppView.as_view(), name='redirect'),
    path('ios/', IosView.as_view(), name='ios'),
    path('android/', AndroidView.as_view(), name='android'),
    path('pc/', PcView.as_view(), name='pc'),
]
