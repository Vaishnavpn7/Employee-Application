from django.shortcuts import render, redirect
from api.models import Employees
from django.views.generic import View, CreateView, ListView
from employee.forms import EmpForm
from django.contrib import messages
from django.urls import reverse_lazy


class EmployeeCreateView(CreateView):
    template_name = 'add-emp.html'
    form_class = EmpForm
    success_url = reverse_lazy('list-emp')

    def form_valid(self, form):
        messages.success(self.request, 'account created')
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     form = EmpForm
    #     return render(request, 'add-emp.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = EmpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('task-list')
    #     else:
    #         return render(request, 'add-emp.html', {'form': form})


class ListEmp(ListView):
    model = Employees
    template_name = 'list-emp.html'
    context_object_name = 'emp'


class DeleteEmp(View):

    def get(self, request, *args, **kwargs):
        id =kwargs.get('id')
        Employees.objects.get(id=id).delete()
        messages.success(self.request, 'employee-deleted')
        return redirect('list-emp')
