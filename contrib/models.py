from django.db import models


class SampleModel(models.Model):
    title = models.CharField(max_length=50, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'contrib'


class SampleModel2(models.Model):
    title = models.CharField(max_length=50, blank=True)
    sample = models.ForeignKey(SampleModel, related_name="sample2")
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'contrib'
