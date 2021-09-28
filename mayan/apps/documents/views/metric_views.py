from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from mayan.apps.views.generics import SingleObjectCreateView, SingleObjectListView

from ..forms.metric_forms import MetricForm
from ..models.metric import Metric
from ..links.document_links import link_document_metric_create;
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
        return reverse(viewname='documents:document_metric_list')

class MetricListView(SingleObjectListView):
    model = Metric

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        toName = lambda x : x.metric_name
        ctx["name"] = map(toName, Metric.objects.all())
        return ctx

    def get_extra_context(self):
        return {
            ''''hide_link': True,
            'hide_object': False,
            'list_as_items': False,'''
            'no_results_main_link': link_document_metric_create.resolve(
                context=RequestContext(request=self.request)
            ),
            'no_results_text': _(
                'Define a review metric for each axis of assessment'
            ),
            'no_results_title': _('No review metrics available'),
            'title': _('Review Setup'),
        }
