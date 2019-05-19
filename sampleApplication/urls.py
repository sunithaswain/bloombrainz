from django.conf.urls import url
from . import views

urlpatterns = [	    
    url(r'^home/', views.index, name='home'),
    url(r'^step2/', views.step2, name='passport'),
    url(r'^step3/', views.step3, name='allDetails'),
]
