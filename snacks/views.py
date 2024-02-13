from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class AboutPageView(TemplateView):
  template_name = 'about.html'

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack  

# model admin steps
  # python manage.py createsuperuser
  # python manage.py makemigrations snacks
  # python manage.py migrate