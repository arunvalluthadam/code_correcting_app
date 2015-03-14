from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
	
    url(r'^$', 'codetesting_app.views.home', name='home'),
    url(r'^one-question/(?P<question_id>\d+)$', 'codetesting_app.views.one_question', name='one_question'),
    url(r'^answer-valid/$', 'codetesting_app.views.answer_valid', name='answer_valid'),
    url(r'^right-result/$', 'codetesting_app.views.right_result', name='right_result'),
    url(r'^wrong-result/$', 'codetesting_app.views.wrong_result', name='wrong_result'),

)

# reverse('one_question')
