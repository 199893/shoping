from django.conf.urls import url
from . import views

app_name='store'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^offers/$', views.offers, name='offers'),
    url(r'^about/$', views.about, name='about'),
    url(r'^markerplace/$', views.marketplace, name="markerplace"),
    url(r'^values/$', views.values, name='values'),
    url(r'^privacy/$', views.privacy, name="privacy"),




    url(r'^sitemap/$',views.sitemap,name='sitemap'),
    url(r'^help/$',views.help,name='help'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^faq/$', views.faq, name='faq'),




    url(r'^active/(.*?)/$',views.active,name='active'),
	
	
	
	
	
	
	
	
	
	
	url(r'^card/$',views.card,name='card'),
	url(r'^products/$',views.products,name='products'),
    url(r'^single/$',views.single,name='single')
]