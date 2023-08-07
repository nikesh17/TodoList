from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django import forms 
from todofeature.forms import TaskForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from todofeature.models import Task
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.mixins import LoginRequiredMixin
# class TaskCreateView(LoginRequiredMixin,CreateView):
#     #this works like a login_required decorator for class based view

    
def todo_list_view (request):
    tasks = Task.objects.all().order_by("id")
    context = {"tasks": tasks}
    return render(request,"todo_list.html", context)

@login_required
def todo_add_view(request):
    # print(request.POST)
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))
    return render(request, "add_todo.html", {'form':form})

def todo_edit_view(request, taskid):
    task = get_object_or_404(Task, id = taskid)
    # try:
    #     Task.objects.get(id=taskid)
    # except Task.DoesNotExist:
    #     raise Http404()
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))
    return render(request,"add_todo.html",{"form":form})

# def todo_delete_view(request, taskid):
#     task = get_object_or_404(Task, id = taskid)
#     task.delete()
#     return HttpResponseRedirect(reverse("todofeature:todo_list"))

def todo_delete_view(request):
    taskid = request.POST.get('taskid')
    task = get_object_or_404(Task,id=taskid)
    task.delete()
    return HttpResponseRedirect(reverse("todofeature:todo_list"))
    
def demo_for_ajax(request):
    data = {"name": "Ram", "address": "Kathmandu"}
    return JsonResponse(data, safe=False)