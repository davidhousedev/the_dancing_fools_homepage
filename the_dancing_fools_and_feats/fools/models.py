from datetime import timedelta

from django.db import models

EVENT_MAX_TITLE_LENGTH = 100
EVENT_DESCRIPTION_MAX_LENGTH = 150
EVENT_LOCATION_MAX_LENGTH = 60
EVENT_URL_MAX_LENGTH = 300
ONE_WEEK = 7
ONE_MONTH = 30
ONE_YEAR = 365


class DanceEvent(models.Model):
    READABLE_FREQUENCY = 'One-time'
    OCCURRENCE_TIME_FORMAT = '%x'

    title = models.CharField(
        max_length=EVENT_MAX_TITLE_LENGTH,
        help_text=f'User-facing name of the event. '
                  f'max {EVENT_MAX_TITLE_LENGTH} characters')
    occurrence = models.DateField(
        help_text='Example date of this event, used with frequency to '
                  'anticipate when this event will occur in the future. '
                  'format: YYYY-MM-DD')
    website_url = models.URLField(
        max_length=EVENT_URL_MAX_LENGTH,
        help_text=f'Official website of this event. '
                  f'max: {EVENT_URL_MAX_LENGTH} characters')
    location = models.CharField(
        max_length=EVENT_LOCATION_MAX_LENGTH,
        help_text=f'Approximate location of this event, e.g. Newton, MA. '
                  f'max: {EVENT_LOCATION_MAX_LENGTH} characters')
    description = models.TextField(
        max_length=EVENT_DESCRIPTION_MAX_LENGTH,
        help_text=f'User-facing description of this event. '
                  f'max: {EVENT_DESCRIPTION_MAX_LENGTH} characters')
    order = models.IntegerField(
        help_text='Visual order of the event compared to other events. '
                  'Lower numbers will appear atop other events.')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title}, {self.location}'

    @property
    def frequency_str(self):
        return self.READABLE_FREQUENCY

    @property
    def occurrence_str(self):
        return self.occurrence.strftime(self.OCCURRENCE_TIME_FORMAT)


class WeeklyEvent(DanceEvent):
    READABLE_FREQUENCY = 'Weekly'
    OCCURRENCE_TIME_FORMAT = '%A'

    frequency = models.DurationField(
        editable=False, default=timedelta(days=ONE_WEEK))


class MonthlyEvent(DanceEvent):
    READABLE_FREQUENCY = 'Monthly'
    OCCURRENCE_TIME_FORMAT = '%A'

    frequency = models.DurationField(
        editable=False, default=timedelta(days=ONE_MONTH))


class YearlyEvent(DanceEvent):
    READABLE_FREQUENCY = 'Yearly'
    OCCURRENCE_TIME_FORMAT = '%B'

    frequency = models.DurationField(
        editable=False, default=timedelta(days=ONE_YEAR))
