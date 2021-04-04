from django.urls import path
from .views import *

urlpatterns = [
    path('', AbisitaTemplateView.as_view(), name="AbisitaListView"),
]
