from django.urls import path
from novel.views import index,novel_info
urlpatterns = [
    path(r'index/',index),
    path(r'info/',novel_info)
]



