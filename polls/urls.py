from django.conf.urls import url
from . import views

#After it goes through mysite/urls.py, it comes here and 
#polls is stripped from the path. And since there is 
#nothing else it gives us our index function.
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#regex:
#^ = start of string
#() = a group
#?P = match the group to a param; in our case <question_id>
#[0-9]+ = matches 1 or more of the numbers
#$ = end of string