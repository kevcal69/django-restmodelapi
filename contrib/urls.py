from django.conf.urls import url
from contrib import views

urlpatterns = [
    url(
        r'resource/get/$',  #: url regex
        views.ResourceGetAPI.as_view(),  #: view
        name='resource-get-api'),  #: url name
]
