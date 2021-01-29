from django.urls import path
from .views import other
urlpatterns = [
    path('other/', other, name='other'),
]
