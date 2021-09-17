from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    # path('', views.vacancies_list, name='vacancies_list'),
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('agency/vacancies_list', views.VacancyListView.as_view(), name='vacancies_list'),
    path('<int:id>/<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancy-feedback/', views.feedback, name="feedback"),
]
