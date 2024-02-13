from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class HomePageView(TemplateView):
  template_name = 'home.html'

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack  
  context_object_name = 'snacks'
