from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from . import models, forms


class EntryCreateView(CreateView):
    model = models.Entry
    form_class = forms.EntryForm
    template_name = 'entry_form.html'

    def form_valid(self, form):
        entry = form.save(commit=False)
        if not self.request.session.session_key:
            self.request.session.save()
        entry.session_key = self.request.session.session_key
        entry.save()
        return super(EntryCreateView, self).form_valid(form)


class EntryDetailView(DetailView):
    model = models.Entry
    template_name = 'entry_detail.html'
