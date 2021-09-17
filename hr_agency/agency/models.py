from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields

class Vacancy(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=250),
        slug = models.SlugField(max_length=250),
        salary = models.CharField(_('salary'), max_length=250),
        description = models.TextField(_('description'))
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('agency_posts'))
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    available = models.BooleanField(_('available'), default=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'

    def get_absolute_url(self):
        return reverse('agency:vacancy_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title