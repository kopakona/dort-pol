from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Vacancy
from django.views.generic import ListView
from .forms import EmailContactForm, FeedbackForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from parler.utils import get_active_language_choices


class VacancyListView(ListView):
    context_object_name = 'vacancies'
    paginate_by = 3
    template_name = 'agency/vacancy/list.html'
    
    def get_queryset(self):
        self.lang = self.request.LANGUAGE_CODE
        return Vacancy.objects.language(self.lang).filter(available=True)
    

def vacancy_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    vacancy = get_object_or_404(Vacancy, 
                                id=id,
                                translations__language_code=language, 
                                translations__slug=slug, 
                                available=True)
    return render(request, 'agency/vacancy/detail.html', {'vacancy': vacancy})

def index(request):
    return render(request, 'agency/vacancy/index.html')

@csrf_protect
def contacts(request):
    sent = False
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'From Dort-Pol site with Subject: {}'.format(cd['subject'])
            message = '{} from email:{}'.format(cd['message'], cd['email'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_TO, ],
                    fail_silently=False)
            sent = True
    else:
        form = EmailContactForm()
    print(sent)
    return render(request, 'agency/vacancy/contacts.html', {'form': form, 'sent': sent})

@csrf_protect
def feedback(request):
    sent = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'From Dort-Pol site feedback form to vacancy {}'.format(cd['vacancy'])
            message = 'First Name: {}\nLast Name:{}\n'\
                    'Phone: {}\n' \
                    'Email: {}\nAddress: {}\n' \
                    'Age: {}\nExperience: {}\n' \
                    'Qualification: {}\nMessage: {}\n'.format(cd['first_name'], cd['last_name'], cd['phone'],
                                                            cd['email'], cd['address'],
                                                            cd['age'], cd['experience'],
                                                            cd['qualification'], cd['message'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_TO, ],
                    fail_silently=False)
            sent = True
    else:
        form = FeedbackForm()
    print(sent)
    return render(request, 'agency/vacancy/feedback.html', {'form': form, 'sent': sent})
