from django.forms import ModelForm

from . import models


class EntryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['placeholder'] = 'Заголовок'
        self.fields['signature'].widget.attrs['placeholder'] = 'Подпись'
        self.fields['text'].widget.attrs['placeholder'] = 'Ваша история'
        self.fields['text'].widget.attrs['rows'] = 10

    class Meta:
        model = models.Entry
        fields = ('title', 'text', 'signature')