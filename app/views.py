from django.shortcuts import render
from django.views.generic import TemplateView,FormView
# Create your views here.
from app.forms import *
from django.http import HttpResponse

class cbv_tv_context(TemplateView):
    template_name='cbv_tv_context.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #context['name']='Ashu'
        #context['age']=2
        sf=StudentForm()
        context['form']=sf
        return context
    def post(self,request):
        data=StudentForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Inserted data')

class cbv_fv(FormView):
    template_name='cbv_fv.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('inserted the data')