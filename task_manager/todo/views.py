from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


# Create your views here.

class Taskform(forms.Form):
    todo = forms.CharField()


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'todo/index.html', {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task = request.POST['todo']
            request.session["tasks"] += [task]
            # ----------------------------------------------- same work
            # return render(request, 'todo/index.html', {
            #     "tasks": tasks
            # })
            # ------------------------------------------------ same work
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'todo/add.html', {
                "form": form
            })
    return render(request, 'todo/add.html', {
        "form": Taskform(),
    })
