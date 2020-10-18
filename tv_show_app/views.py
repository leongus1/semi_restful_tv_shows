from django.shortcuts import render, HttpResponse, redirect
from tv_show_app.models import Shows
import datetime

# Create your views here.

def all_shows(request):
    context = {
        'all_shows': Shows.objects.all(),
    }
    return render(request, 'index.html',context)

def show_details(request, show_id):
    context = {
        'this_show' : Shows.objects.get(id=show_id),
    }
    return render(request, 'show_details.html', context)

def edit_show(request, show_id):
    head = f"Edit Show #{show_id}"
    context = {
        "header": head,
        "this_show": Shows.objects.get(id=show_id),
        "update": "Update",
        "path": f"/shows/{show_id}/update",
        
    }
    return render(request, "add_edit_show.html", context)

def enter_show(request):
    context = {
        "header": "Add a New Show",
        "update": "Create",
        "path": "add/",
    }
    return render(request, 'add_edit_show.html', context)

def add_new(request):
    Shows.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release'], desc = request.POST['description'] )
    show_id = Shows.objects.get(title = request.POST['title'])
    return redirect ('/',show_id)

def destroy(request, show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect('/')

def update_show(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    this_show.title=request.POST['title']
    this_show.network = request.POST['network']
    if not request.POST['release']=="":
        this_show.release_date=request.POST['release']
    this_show.desc = request.POST['description']
    this_show.modified_at = datetime.datetime.now()
    this_show.save()
    this_path = f"/shows/{show_id}"
    
    return redirect(this_path)