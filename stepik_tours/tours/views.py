from django.views.generic import TemplateView
import data
from random import randrange
from django.http import HttpResponseNotFound


def custom_handler404(request, exception):
    return HttpResponseNotFound('К сожалению не удалось найти указанную страницу :(')


class MainView(TemplateView):
    template_name = 'tours/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['title'] = data.title
        context['tours'] = {}
        for i in range(6):
            j = randrange(1, 16)
            context['tours'][j] = data.tours[j]
        context['description'] = data.description
        context['departures'] = data.departures
        context['subtitle'] = data.subtitle
        return context


class DepartureView(TemplateView):
    template_name = 'tours/departure.html'

    def get_context_data(self, **kwargs):
        context = super(DepartureView, self).get_context_data(**kwargs)
        context['title'] = data.title
        context['tours'] = {}
        for key in [key for key, tour in data.tours.items()
                    if tour['departure'] == context['departure']]:
            context['tours'][key] = data.tours[key]
        context['departures'] = data.departures
        context['departure'] = data.departures[context['departure']]
        return context


class TourView(TemplateView):
    template_name = 'tours/tour.html'

    def get_context_data(self, **kwargs):
        context = super(TourView, self).get_context_data(**kwargs)
        context['tour'] = data.tours[kwargs['pk']]
        context['title'] = data.title
        context['departure'] = data.departures[context['tour']['departure']]
        context['departures'] = data.departures
        return context
