from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from explorer.models import DataEm
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import explorer.base.search_form as sf
from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic.edit import FormMixin


class IndexView(generic.ListView):
    template_name = 'explorer/index.html'
    context_object_name = 'apps_list'

    def get_queryset(self):
        """Return the last fifty apps."""
        return DataEm.objects.order_by('-id')[:50]


class DetailView(generic.DetailView):
    model = DataEm
    template_name = 'explorer/index.html'


# the only way is if we wrote it into a database and read it from the other side but that would be wrong!!


class ResultsView(generic.ListView):
    model = DataEm
    template_name = 'explorer/results.html'
    context_object_name = 'apps'
    paginate_by = 10

    def get_queryset(self):
        print "here"
        apps = get_data(self.request)
        return apps


class SearchView(generic.FormView):
    template_name = 'explorer/search.html'
    form_class = sf.SearchForm
    success_url = '/explorer/resutls/'


# Trying to mix the two views in one
class SearchView__(generic.FormView):
    template_name = 'explorer/search.html'
    form_class = sf.SearchForm
    success_url = '/explorer/search/'

    model = DataEm
    paginate_by = 10
    context_object_name = 'apps'

    def get_queryset(self):
        print "we're here"
        apps = get_data(self.request)
        return apps


def get_data(request):
    try:
        name = request.GET['app_title']
        price = request.GET['price']
        content_rating = request.GET['content_rating']
        downloads = request.GET['downloads']
        user_rating = request.GET['rating']
        category = request.GET['category']
        cluster = request.GET['cluster']
        language = request.GET['language']
    except:
        return []
    apps = []

    if len(name) != 0:
        apps = DataEm.objects.filter(title__icontains=name)

    if price != 'all':
        if price == 'free':
            temp_apps = DataEm.objects.filter(price=0)
        else:
            temp_apps = DataEm.objects.filter(price__gt=0)
        apps = verify(apps, temp_apps)

    if content_rating != 'All':
        temp_apps = DataEm.objects.filter(content_rating=content_rating)
        apps = verify(apps, temp_apps)

    if downloads != 'All':
        temp_apps = DataEm.objects.filter(downloads=downloads)
        apps = verify(apps, temp_apps)

    if user_rating != 'Any':
        if user_rating == '>1':
            temp_apps = DataEm.objects.filter(rating__gte=1.0)
        elif user_rating == '>2':
            temp_apps = DataEm.objects.filter(rating__gte=2.0)
        elif user_rating == '>3':
            temp_apps = DataEm.objects.filter(rating__gte=3.0)
        elif user_rating == '4':
            temp_apps = DataEm.objects.filter(rating__gte=4.0)
        else:
            temp_apps = DataEm.objects.filter(rating=5)
        apps = verify(apps, temp_apps)

    if category != 'All':
        temp_apps = DataEm.objects.filter(category=category)
        apps = verify(apps, temp_apps)

    if cluster != 'Any':
        temp_apps = DataEm.objects.filter(cluster_id=cluster)
        apps = verify(apps, temp_apps)

    if language != 'All':
        if language == 'other':
            temp_apps = DataEm.objects.filter(~Q(lang_id='ar') & ~Q(lang_id='en'))
        else:
            temp_apps = DataEm.objects.filter(lang_id=language)

        apps = verify(apps, temp_apps)
        # if no criteria specified, return everything:
    if len(name) == 0 and price == 'all' and content_rating == 'All' and downloads == 'All' and user_rating == 'Any' and category == 'All' and cluster == 'Any' and language == 'All':
        apps = DataEm.objects.all()
    return apps


def verify(apps, temp_apps):
    if len(apps) == 0:
        apps = temp_apps
    else:
        apps = apps & temp_apps
    return apps


def process_search(request):
    return "FCK!"
    # return HttpResponseRedirect(reverse('explorer:results'))
