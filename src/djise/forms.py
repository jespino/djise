from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from djise.models import Activity

class ProposalForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'description', 'event')
        widgets = {'event': HiddenInput}
