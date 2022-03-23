from multiprocessing import context
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from adminssion.forms import AdminssionForm
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from adminssion.models import Adminssion

# Create your views here.
def home(request):
    if request.method=="POST":
        form=AdminssionForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.save()
            return redirect('crud:home_page')
    else:
        form=AdminssionForm()
        context={
            'form':form
        }
        
    return render(request,'index.html',context)

class StudentCreateView(CreateView):
    model=Adminssion
    form_class=AdminssionForm
    template_name='index.html'
    success_url=reverse_lazy('crud:home_page')

    
    

def edit_student(request,id):
    data=Adminssion.objects.get(id=id)
    form=AdminssionForm(request.POST or None, instance=data)
    if form.is_valid():
        form=form.save(commit=False)
        form.save()
        return redirect('crud:student_list')
    
    context={
        'form':form
    }
    return render(request,'update.html',context)
        

class StudentListView(ListView):
    model=Adminssion
    template_name='student_list.html'
    context_object_name='students'
    
class StudentUpdateView(UpdateView):
    model=Adminssion
    template_name='update.html'
    form_class=AdminssionForm
    def get_success_url(self):
        return reverse_lazy('crud:student_list')

class StudentDeleteView(DeleteView):
    model=Adminssion
    template_name='delete_student.html'
    success_url=reverse_lazy('crud:student_list')
    
    
    
    

   
