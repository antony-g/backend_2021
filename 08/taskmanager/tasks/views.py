from django.http import JsonResponse
from django.shortcuts import render
from .decorators import login_required
from datetime import date, timedelta
from .models import Task
from .forms import PostForm


# URL /login/
def login(request):
	return render(request, 'login.html')


# URL /
@login_required
def login_home(request):
	print(request.user)
	return render(request, 'home.html')


# URL /api/all/
def _api_all_tasks(request):
	tasks = Task.objects.all()
	data = [{'id': task.id, 'description': task.description, 'due': task.due,} for task in tasks]
	return JsonResponse({'tasks': data})


# URL /api/all/
@login_required
def api_all_tasks(request):
	tasks = Task.objects.filter(user=request.user)
	return JsonResponse({'tasks': [{'id': task.id, 'description': task.description, 'due': task.due} for task in tasks]})


# URL /api/new/
def api_new_task(request):
	form = PostForm(request.POST)
	if form.is_valid():
		task = Task(user=request.user,
					description=request.data['description'],
					due=date.today() + timedelta(days=int(request.data['due_in'])))
		post = form.save()
		return JsonResponse({'done': True, 'id': post.id}, status=200)
	else:
		return JsonResponse({'done': False, 'errors': form.errors}, status=400)


# URL /api/update/
def api_update_task(request):
	form = PostForm(request.POST)
	if form.is_valid():
		task = request.user.task_set.get(id=int(request.data['task_id']))
		try:
			task.description = request.data['description']
		except:
			pass
		try:
			task.due = date.today() + timedelta(days=int(request.data['due_in']))
		except:
			pass
		post = task.save()
		return JsonResponse({'done': True, 'id': post.id}, status=200)
	else:
		return JsonResponse({'done': False, 'errors': form.errors}, status=400)


# URL /api/delete/
def api_delete_task(request):
	task = request.user.task_set.get(id=int(request.data['task_id']))
	task.delete()
	return JsonResponse({'done': True})