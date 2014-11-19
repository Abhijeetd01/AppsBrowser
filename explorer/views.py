from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from explorer.models import DataEm
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import explorer.base.search_form as sf
from django.shortcuts import render_to_response


class IndexView(generic.ListView):
    template_name = 'explorer/index.html'
    context_object_name = 'apps_list'

    def get_queryset(self):
        """Return the last fifty apps."""
        return DataEm.objects.order_by('-id')[:50]


class DetailView(generic.DetailView):
    model = DataEm
    template_name = 'explorer/index.html'


class ResultsView(generic.ListView):
    print "Soemthing"
    model = DataEm
    template_name = 'explorer/results.html'
    context_object_name = 'apps'


#the only way is if we wrote it into a database and read it from the other side but that would be wrong!!

class SearchView(generic.FormView):
    template_name = 'explorer/search.html'
    form_class = sf.SearchForm
    success_url = '/explorer/results/'


    # response_class = ResultsView

    # def form_valid(self, form):
    #     print "validating..."
    #     # name = form.cleaned_data['App_title']
    #     # apps = DataEm.objects.filter(title__contains=name)
    #     # print type(apps)
    #     # for app in apps:
    #     # print "%s %s %s %s %s" % (app.title, app.developer, app.price, app.category, app.cluster_id)
    #     # # return HttpResponseRedirect(reverse('explorer:results', args=(apps,)))
    #     # # return redirect('explorer:results', apps)
    #     return render_to_response('explorer/results.html', get_data(form))

    # def done(self, form):
    #     return render_to_response('explorer/results.html', get_data(form))


def get_data(form):
    name = form.cleaned_data['App_title']
    apps = DataEm.objects.filter(title__contains=name)
    return apps


def process_search(request):
    return "FCK!"
    # return HttpResponseRedirect(reverse('explorer:results'))
