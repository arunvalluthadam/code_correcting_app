from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

import code_for_test
import unittest

# Create your views here.
def home(request):
	questions = Questions.objects.all()
	variables = RequestContext(request, {
		'questions': questions,
	})
	return render_to_response('index.html', variables)

lis = []

@csrf_exempt
def one_question(request, question_id=1):
	questions = Questions.objects.get(id=question_id)
	inner_dict = {'test_question':questions.test_function, 'test_answer': questions.expected_ans}
	lis.append(inner_dict)
	if request.method == "POST":
		form = QuestForm(request.POST)
		if form.is_valid():
			code_ans = form.save(commit=False)
			code_ans.your_code = request.POST['quest']
			code = code_ans.your_code
			print code
			print "Use sum_of_multiples as function name"
			code_ans.save()
			
		else:
			print form.errors
	else:
		form = QuestForm()
	
	variables = RequestContext(request, {
		'one_questions': questions,
		# 'form': form,
	})
	return render_to_response('one-question.html', variables)

def answer_valid(request):
	code = request.POST.get('quest', '')
	file = open("codetesting_app/code_for_test.py", "w")
	file.write(code)
	file.close()
	print "data writed"

	got = code_for_test.lis[-1]['test_question']
	expected = lis[-1]['test_answer']

	if got == expected:
		return HttpResponseRedirect('/right-result')
	else:
		return HttpResponseRedirect('/wrong-result')


def right_result(request):
	return render_to_response('right-result.html')

def wrong_result(request):
	return render_to_response('wrong-result.html')