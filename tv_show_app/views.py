from django.shortcuts import render, HttpResponse, redirect
from tv_show_app.models import Shows, ShowManager
import datetime
from django.contrib import messages

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
        "path": "/shows/create/",
    }
    return render(request, 'add_edit_show.html', context)

def add_new(request):
    errors = Shows.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')
    else: 
        Shows.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release'], desc = request.POST['description'] )
        show_id = Shows.objects.get(title = request.POST['title'])
        show_id = show_id.id
        messages.success(request, "Show successfully created!")
        return redirect (f'/shows/{show_id}')

def destroy(request, show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect('/')

def update_show(request, show_id):
    errors = Shows.objects.validator(request.POST)
    if not Shows.objects.get(id=show_id).title == request.POST['title']:
        if Shows.objects.filter(title=request.POST['title']).count()>0:
                errors['title_duplication'] = "There is already a show with this name in the database"
        
    
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit/')
    else: 
        this_show = Shows.objects.get(id=show_id)
        this_show.title=request.POST['title']
        this_show.network = request.POST['network']
        if not request.POST['release']=="":
            this_show.release_date=request.POST['release']
            
        this_show.desc = request.POST['description']
        this_show.save()
        messages.success(request, "Show successfully updated!")
        return redirect(f"/shows/{show_id}")

def default(request):
    return redirect('/shows')