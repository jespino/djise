from supertools.views.menu import MenuMixin
from django.views.generic import TemplateView, View, DetailView, ListView
from django.http import HttpResponse
from djise.models import Entity, Event, Activity
from django.core import serializers
from djise.forms import ProposalForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class DetailSuperView(MenuMixin, DetailView):
    menu = []


class ListSuperView(MenuMixin, ListView):
    menu = []


class EventView(MenuMixin, TemplateView):
    template_name = "djise/event_detail.html"
    menu = ['events']

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug)
        context['proposal_form'] = ProposalForm(initial={'event': context['object']})
        return self.render_to_response(context)

    def post(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug)
        proposal_form = ProposalForm(request.POST, initial={'event': context['object']})
        context['proposal_form'] = proposal_form
        if proposal_form.is_valid():
            proposal_form.save()
            messages.success(request, _('Proposal sended.'))
            return self.render_to_response(context)
        return self.render_to_response(context)

    def get_context_data(self, slug, *args, **kwargs):
        context = {}
        context['object'] = Event.objects.get(slug=slug)
        return context

class VoteView(View):
    def get(self, request, slug, *args, **kwargs):
        if not request.session.get(slug, None):
            activity = Activity.objects.get(slug=slug)
            activity.votes += 1
            activity.save()
            messages.success(request, _('Activity voted.'))
            request.session[slug] = True
        else:
            messages.error(request, _('You have already voted this activity.'))

        return HttpResponseRedirect(reverse('activity', args=[slug]))
