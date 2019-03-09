from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import User

class UserList(ListView):
    model = User

class UserDetail(DetailView):
    model = User


class UserCreation(CreateView):
    model = User
    success_url = reverse_lazy('users:new')
    fields = ['name', 'start_date', 'end_date', 'description']

class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users:edit')
    fields = ['name', 'start_date', 'end_date', 'description']


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users:delete')