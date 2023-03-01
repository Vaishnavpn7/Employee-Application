from django.urls import path
from employee import views

urlpatterns = [
    path('emp', views.EmployeeCreateView.as_view(), name='add-emp'),
    path('emp/view', views.ListEmp.as_view(), name='list-emp'),
    path('emp/<int:id>',views.DeleteEmp.as_view(), name='delete-emp')


]
