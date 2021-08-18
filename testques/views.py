from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Group, Option, Question
# Create your views here.

def home(request):
	return render(request, 'base.html')

# def index(request):
# 	"""
# 	index function for test/
# 	"""
# 	test_groups = Group.objects.all()
# 	context = {
# 			   'groups':test_groups
# 				}
# 	return render(request, 'index.html', context)

class IndexView(generic.ListView):
	"""
	index-view for test
	"""
	model = Group
	template_name = 'index.html'
	context_object_name = 'groups'

	def get_queryset(self):
		return Group.objects.all()



# def detail(request, test_id):
# 	"""
# 	page for test/<test-d>
# 	"""

# 	test_group = Group.objects.get(id=test_id)
# 	print(type(test_group))
# 	# breakpoint()
# 	questions_qs = test_group.question.all()

# 	context = {'question_qs':questions_qs}

# 	return render(request, 'detail.html',context)

class DetailView(generic.DetailView):
	model = Group
	template_name = 'detail.html'


def create(request, methods=['POST', 'GET']):
	
	if request.method=="POST":
		# print(request.POST)
		# <QueryDict: {'csrfmiddlewaretoken': ['Jbh8BLlvcLnoVSM00ocKm8TNiiznS7phIqDPsEcWaDxNR92ITNYWMlZZHiNs7j5r'], 
		# 'ques_text': ['q3'], 'op1': ['abc'], 'op2': ['def'], 'op3': ['ghi'], 'op4': ['jkl'], 
		# 'Submit': ['Generate']}>
		err = {'error': "Error occured. Check your data is complete"}

		if  request.POST.get('op1') == "" or   request.POST.get('op2') == "" or   request.POST.get('op3') == "" or request.POST.get('op4') == "":
			return render(request, 'create.html' ,err)
		else:
			question_text = request.POST.get('ques_text')
			options = []
			options.append(request.POST.get('op1'))
			options.append(request.POST.get('op2'))
			options.append(request.POST.get('op3'))
			options.append(request.POST.get('op4'))

			question = Question(question_text=question_text)
			question.save()

			for option in options:
				option_ob = Option.objects.create(question=question, option_text=option)
				option_ob.save()

			group_name = request.POST.get('group')
			# breakpoint()

			group_object = Group.objects.get(group_name=group_name)
			group_object.question.add(question)

			return redirect(reverse('index'))
	else:
		groups_qs = Group.objects.all()
		groups = []
		for grp in groups_qs:
			groups.append(grp.group_name)
		context = {'groups':groups}
		return render(request, 'create.html',context)
