from .models import Page
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class PageListView(ListView):
    model = Page

class  PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')

class PageUpdate(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'
    
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')