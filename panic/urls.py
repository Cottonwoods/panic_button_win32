from django.conf.urls import patterns, url

from panic import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^panic/$', views.panic, name='panic'),
)
