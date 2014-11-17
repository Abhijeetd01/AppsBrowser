from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from explorer.models import DataEm
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'explorer/index.html'
    context_object_name = 'apps_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return DataEm.objects.order_by('-id')[:50]


class DetailView(generic.DetailView):
    model = DataEm
    template_name = 'explorer/index.html'