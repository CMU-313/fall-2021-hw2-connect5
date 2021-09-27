from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models.reviewer import Reviewer
from ..models.applicant import Applicant
from ..models.review import Review
from ..models.metric import Metric


class ReviewForm(forms.Form):
    reviewer = forms.CharField(label='Reviewer Name', max_length=30)
    applicant = forms.CharField(label='Applicant Name', max_length=30)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

        # Dynamically create the fields
        metrics = self.get_metrics()
        for metric in metrics:
            self.fields[metric] = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    def save(self, document):
        reviewer, _ = Reviewer.objects.get_or_create(
            name=self.cleaned_data['reviewer']
        )

        applicant, _ = Applicant.objects.get_or_create(
            name=self.cleaned_data['applicant'],
            document=document
        )

        # Serialize the rating results
        evaluation = ''
        metrics = self.get_metrics()
        for metric in metrics:
            evaluation += f'{metric}:{self.cleaned_data[metric]}\n'

        review = Review.objects.create(
            reviewer=reviewer,
            applicant=applicant,
            evaluation=evaluation
        )

    def get_metrics(self):
        metric_objects = Metric.objects.all()
        metrics = [x['metric_name'] for x in metric_objects]
        return metrics
