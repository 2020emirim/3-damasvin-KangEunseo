from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from menu.models import Drink, Coffee, Bubbletea


class DrinkListView(ListView):  # drink_list.html
    model = Drink
    # paginate_by = 3


class CoffeeCreateView(CreateView):  # bookmark_form.html - form 이름이 흔해서 아래처럼 create로 바꿔준 거
    model = Coffee
    fields = '__all__'  # ['category', 'name', 'price', 'image']
    template_name = 'menu/drink_create.html'
    success_url = reverse_lazy('menu:list')
    initial = {'category': 'Coffee'}


class BubbleteaCreateView(CreateView):  # bookmark_form.html - form 이름이 흔해서 아래처럼 create로 바꿔준 거
    model = Bubbletea
    fields = '__all__'  # ['category', 'name', 'price', 'image']
    template_name = 'menu/drink_create.html'
    success_url = reverse_lazy('menu:list')
    initial = {'category': 'Bubbletea'}


class DrinkUpdateView(UpdateView):
    model = Drink
    fields = '__all__'
    template_name_suffix = '_update'  #drink_update.html
    success_url = reverse_lazy('menu:list')


class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = reverse_lazy('menu:list')
