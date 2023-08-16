from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AdvertFilter, ReactionFilter, UserAdvertFilter
from .forms import AdvertsForm, ReactionForm
from .models import Post, Reaction


class AdvertsList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'adverts.html'
    context_object_name = 'adverts'   # имя списка, где все объекты; чтобы обратиться в html-шаблоне
    paginate_by = 10

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class UserAdvertsList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'user_adverts.html'
    context_object_name = 'user_adverts'  # имя списка, где все объекты; чтобы обратиться в html-шаблоне
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        self.filterset = UserAdvertFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        print(context)
        return context


class AdvertDetail(DetailView):
    model = Post
    template_name = 'advert.html'
    context_object_name = 'advert'
    queryset = Post.objects.all()


class AdvertCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('advert.add_post',)
    form_class = AdvertsForm
    model = Post
    template_name = 'advert_edit.html'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        return super().form_valid(new_post)

    def get_success_url(self):
        return reverse_lazy('adverts_list')


class AdvertEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('advert.change_post',)
    form_class = AdvertsForm
    model = Post
    template_name = 'advert_edit.html'


class AdvertDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('advert.delete_post',)
    model = Post
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('adverts_list')


class ReactionCreate(CreateView):
    permission_required = ('advert.add_reaction',)
    form_class = ReactionForm
    model = Reaction
    template_name = 'reaction_create.html'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.post = Post.objects.get()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('adverts_list')


class ReactionsList(ListView):
    model = Reaction
    ordering = '-created_at'
    template_name = 'reactions.html'
    context_object_name = 'reactions'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReactionFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


