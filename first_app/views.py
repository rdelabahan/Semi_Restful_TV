from django.shortcuts import render, redirect
from first_app.models import Show
from django.contrib import messages

def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request,'index.html',context)

def create(request):
    return render(request,'create.html')

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/create")
    else:
        new_show = Show.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            release_date = request.POST["date"],
            description = request.POST["description"],
        )
    return redirect(f"/display_show/{new_show.id}")

def display_show(request, show_id):
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request,"show.html",context)

def delete(request, show_id):
    del_show = Show.objects.get(id = show_id)
    del_show.delete()
    return redirect("/")

def edit(request, show_id):
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request,"edit.html",context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/edit_show/{show_id}")
    else:
        updated_show = Show.objects.get(id = show_id)
        updated_show.title = request.POST["title"]
        updated_show.network = request.POST["network"]
        updated_show.release_date = request.POST["date"]
        updated_show.description = request.POST["description"]
        updated_show.save()
        return redirect(f"/display_show/{show_id}")
