

from django.shortcuts import render, redirect
from .forms import School
from MyApp.models import School
# Create your views here.
def emp(request):
    if request.method == 'POST':
        form = School(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form=School()
        return render(request,'index.html',{'form':form})
def show(request):
    school = School.objects.all()
    return render(request,'show.html',{'schools':School})
def edit(request, id):
    school = School.objects.get(id=id)
    return render(request,'edit.html',{'school':School})
def update(request, id):
    school = School.objects.get(id=id)
    form = School(request.POST,instance=school)
    if form.is_valid():
       form.save()
       return redirect("/show")
    return render(request,'edit.html',{'school':school})
def destroy(request, id):
    school = School.objects.get(id=id)
    school.delete()
    return redirect("/show")




