from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from mayan.apps.views.generics import SingleObjectCreateView

from ..forms.metric_forms import MetricForm
from ..permissions import permission_metric_create

class MetricCreateView(SingleObjectCreateView):
    form_class = MetricForm
    object_permission = permission_metric_create

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(redirect_to=self.get_success_url())

    def get_extra_context(self):
        return {
            'title': _('Create Admission Metrics'),
        }

    def get_instance_extra_data(self):
        return {
            '_event_actor': self.request.user
        }

    def get_post_action_redirect(self):
        return reverse(viewname='common:home')
