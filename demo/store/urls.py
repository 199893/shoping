from django.conf.urls import url
from . import views

app_name='store'
urlpatterns = [
    url('^$',views.index,name='index')
]