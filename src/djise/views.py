from django.views.generic import TemplateView
from django.http import HttpResponse
from djise.models import Entity, Event
from django.core import serializers
from djise.forms import ProposalForm

class EventView(TemplateView):
    template_name = "djise/event_detail.html"

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
            return self.render_to_response(context)
        return self.render_to_response(context)

    def get_context_data(self, slug, *args, **kwargs):
        context = {}
        context['object'] = Event.objects.get(slug=slug)
        return context
