
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from idgo_lme_majic.views import MajicCreate
from idgo_lme_majic.views import LmeCreate
from idgo_lme_majic.views import home

from idgo_lme_majic.views.majic import majic_check
from idgo_lme_majic.views.majic import download_majic
from idgo_lme_majic.views.majic import geojson

# from django.urls import re_path

app_name = 'idgo_lme_majic'

router = DefaultRouter()

urlpatterns = [
   url('^$', home, name='home'),

   url('^majic/?$', MajicCreate.as_view(), name='majic'),

   url('^lme/?$', LmeCreate.as_view(), name='lme'),

   url(r'^majic_check/?$', majic_check, name='majic_check'),

   url(r'^download_majic/?$', download_majic, name='download_majic'),

   url(r'^geojson/?$', geojson, name='geojson'),
   
   

  
]

urlpatterns += router.urls