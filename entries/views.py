from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

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


class EntryUpdateView(UserPassesTestMixin, UpdateView):
    model = models.Entry
    form_class = forms.EntryForm
    template_name = 'entry_form.html'

    def test_func(self):
        user_session_key = self.request.session.session_key
        entry_session_key = self.get_object().session_key
        return user_session_key == entry_session_key


class EntryDetailView(DetailView):
    model = models.Entry
    template_name = 'entry_detail.html'
