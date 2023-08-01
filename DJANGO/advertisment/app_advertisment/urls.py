from django.urls import path
from .views import index, top_seller


urlpatterns = [
    path("", index, name='main_page'),
    path("top-sellers/", top_seller, name='top_sellers')
]
