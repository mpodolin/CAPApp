from django.shortcuts import render
from .models import Cadet
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    context_dict = {'leadership': current_cadet.leadership_test,
                    'drill': current_cadet.drill_test,
                    'aerospace': current_cadet.aerospace_test,
                    'character': current_cadet.character_development,
                    'fitness': current_cadet.fitness_test,
                    'sda': current_cadet.sda,
                    'speech': current_cadet.speech,
                    'essay': current_cadet.essay,
                    'age': current_cadet.get_age(),
    }
    return render(request, 'promotions/index2.html', context_dict)


@login_required()
def profile(request):
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    context_dict = {'last_name': current_cadet.last_name,
                    'capid': current_cadet.cap_id,
                    'rank': current_cadet.current_rank,
                    'time_in_grade': current_cadet.weeks_in_grade(),
                    }
    return render(request, 'promotions/profile.html', context_dict)


@login_required()
def pt(request):
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    context_dict = {'sit_and_reach': current_cadet.sit_and_reach_requirement(),
                    'sit_ups': current_cadet.sit_up_requirement(),
                    'push_ups': current_cadet.push_up_requirement(),
                    'mile_run': current_cadet.mile_requirement(),
                    }
    return render(request, 'promotions/pt.html', context_dict)