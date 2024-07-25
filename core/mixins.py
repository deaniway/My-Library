from django.contrib.auth import login
from apps.users.forms import ReaderRegisterForm


class UserFormMixin:
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['reader_form'] = ReaderRegisterForm(self.request.POST)
        else:
            data['reader_form'] = ReaderRegisterForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        reader_form = context['reader_form']
        if reader_form.is_valid():
            response = super().form_valid(form)
            self.object.is_reader = True
            self.object.save()
            reader = reader_form.save(commit=False)
            reader.user = self.object
            reader.save()
            login(self.request, self.object)
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))
