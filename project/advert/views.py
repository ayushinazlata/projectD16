from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AdvertFilter, ReactionFilter, UserAdvertFilter
from .forms import AdvertsForm, ReactionForm
from .models import Post, Reaction
from .signals import reaction_created


class AdvertsListView(ListView):
    model = Post
    template_name = 'adverts.html'
    context_object_name = 'adverts'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Post.objects.filter(~Q(author=self.request.user))
        else:
            queryset = super().get_queryset()
        self.filterset = AdvertFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class UserAdvertsListView(ListView):
    model = Post
    template_name = 'user_adverts.html'
    context_object_name = 'user_adverts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        self.filterset = UserAdvertFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdvertDetailView(DetailView):
    model = Post
    template_name = 'advert.html'
    context_object_name = 'advert'
    queryset = Post.objects.all()


class AdvertCreateView(LoginRequiredMixin, CreateView):
    form_class = AdvertsForm
    model = Post
    template_name = 'advert_update.html'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        return super().form_valid(new_post)

    def get_success_url(self):
        return reverse_lazy('adverts_list')


class AdvertUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AdvertsForm
    model = Post
    template_name = 'advert_update.html'


class AdvertDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('adverts_list')


class ReactionCreateView(LoginRequiredMixin, CreateView):
    form_class = ReactionForm
    model = Reaction
    pk_url_kwarg = 'advert_id'
    template_name = 'reaction_create.html'

    def form_valid(self, form):
        new_reaction = form.save(commit=False)
        new_reaction.post = Post.objects.get(pk=self.kwargs['advert_id'])
        new_reaction.author = self.request.user
        reaction_created(new_reaction, created=True)
        return super().form_valid(new_reaction)

    def get_success_url(self):
        return reverse_lazy('adverts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advert_id'] = self.kwargs['advert_id']
        return context


class ReactionsListView(LoginRequiredMixin, ListView):
    model = Reaction
    template_name = 'reactions.html'
    context_object_name = 'reactions'
    paginate_by = 10

    def get_queryset(self):
        queryset = Reaction.objects.filter(post__author=self.request.user)
        self.filterset = ReactionFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


class ReactionsDeleteView(LoginRequiredMixin, DeleteView):
    model = Reaction
    template_name = 'reaction_delete.html'
    success_url = reverse_lazy('reactions_list')


def approved(request, reaction_id):
    Reaction.objects.filter(id=reaction_id).update(is_approved=True)
    reaction = Reaction.objects.get(id=reaction_id)
    post = reaction.post
    user = request.user
    send_mail(
        subject='Пользователь принял ваш отклик!',
        message=f'{user.username}, ваш отклик на объявление {post} принят пользователем {post.author}',
        from_email=None,
        recipient_list=[user.email],
    )
    return redirect('/adverts/')

