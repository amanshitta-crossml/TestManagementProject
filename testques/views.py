from django.shortcuts import render
from django.http import HttpResponse

from .models import Group, Option
# Create your views here.


def index(request):
	"""
	index function for test/
	"""
	test_groups = Group.objects.all()
	context = {
			   'groups':test_groups
				}
	return render(request, 'index.html', context)


def detail(request, test_id):
	"""
	page for test/<test-d>
	"""

	test_group = Group.objects.get(id=test_id)
	print(type(test_group))
	# breakpoint()
	questions_qs = test_group.question.all()

	context = {'question_qs':questions_qs}

	return render(request, 'detail.html',context)