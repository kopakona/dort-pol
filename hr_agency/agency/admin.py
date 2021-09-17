from django.contrib import admin
from .models import Vacancy
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableModelForm


class VacancyAdminForm(TranslatableModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label=_('description'))

    class Meta:
        model = Vacancy
        fields = '__all__'


@admin.register(Vacancy)
class VacancyAdmin(TranslatableAdmin):
    form = VacancyAdminForm
    list_display = ('title', 'author', 'publish', 'available', 'slug')
    list_filter = ('created', 'publish', 'author', 'available')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish', 'available')
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}