from django import forms

import json

from ..models.reviewer import Reviewer
from ..models.applicant import Applicant
from ..models.review import Review
from ..models.metric import Metric


class ReviewForm(forms.Form):

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

        try:
            applicant = Applicant.objects.get(document=document)
        except (Applicant.DoesNotExist, Applicant.MultipleObjectsReturned):
            max_name = Applicant._meta.get_field('name').max_length
            try:
                name = document.label[:document.label.index('.')]
            except ValueError:
                name = document.label
            
            applicant, _ = Applicant.objects.get_or_create(
                name=name[:max_name],
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
