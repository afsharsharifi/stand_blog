from blog.models import Article
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView, UpdateView)

from home.forms import ContactUsForm

from .models import Message

# Create your views here.


def sidebar_partial(request):
    context = {
        'name': "Afshar Sharifi",
    }
    return render(request, 'includes/sidebar.html', context)


def index_page(request):
    articles = Article.objects.get_active_items()
    context = {
        "articles": articles,
    }
    return render(request, 'home/index.html', context)


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title += " Added"
            instance.save()
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'home/contact.html', context)


class ContactUsView(FormView):
    template_name = "home/contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form_data = form.cleaned_data
        # Message.objects.create(title=form_data["title"], text=form_data["text"], email=form_data["email"])
        Message.objects.create(**form_data)
        return super().form_valid(form)


class MessageView(CreateView):
    model = Message
    fields = ("title", "text")
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        print(self.object)
        return super().get_success_url()


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("title", "text")
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("messages_list")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("messages_list")
