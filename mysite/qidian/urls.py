from django.urls import path
from qidian.views import index,qidian_contain
urlpatterns = [
    path(r'index/',index),
    path(r'contain/',qidian_contain)
]