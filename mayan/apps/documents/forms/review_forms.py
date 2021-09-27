from django import forms

import json

from ..models.reviewer import Reviewer
from ..models.applicant import Applicant
from ..models.review import Review
from ..models.metric import Metric


class ReviewForm(forms.Form):
    applicant = forms.CharField(label='Applicant Name', max_length=30)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

        # Dynamically create the choice fields with rating options from 1 to 5
        metrics = self.get_metrics()
        for metric in metrics:
            self.fields[metric] = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
        self.fields['additional-comments'] = forms.CharField(label='Additional Comments', max_length=500, required=False, widget=forms.Textarea())

    def save(self, reviewer_name, document):
        reviewer, _ = Reviewer.objects.get_or_create(
            name=reviewer_name
        )

        applicant, _ = Applicant.objects.get_or_create(
            name=self.cleaned_data['applicant'],
            document=document
        )

        del self.cleaned_data['applicant']
        review = Review.objects.create(
            reviewer=reviewer,
            applicant=applicant,
            evaluation=json.dumps(self.cleaned_data) # Serialized evaluations
        )

    def get_metrics(self):
        return [x.metric_name for x in Metric.objects.all()]
