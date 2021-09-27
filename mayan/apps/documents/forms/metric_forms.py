from django import forms

from ..models.metric import Metric


class MetricForm(forms.Form):
    metrics = forms.CharField(label='Metrics (Comma-Separated, example shown below)', initial="School Rating, GPA Rating, Research Rating", widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

    def save(self):
        metrics = map(lambda x: x.strip(), self.cleaned_data['metrics'].split(','))
        for metric in metrics:
            Metric.objects.update_or_create(metric_name=metric)
