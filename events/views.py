from django.shortcuts import render
from .models import Event
from promotions.models import Cadet
from django.utils import timezone

# Selects the next weekly meeting of the squadron for the call down
def call_down(request):
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    current_squadron = current_cadet.squadron
    next_meeting = Event.objects.filter(squadron__iexact=current_squadron)
    next_meeting = next_meeting.filter(weekly_meeting__exact=True)
    next_meeting = next_meeting.filter(start__gte=timezone.now())
    next_meeting = next_meeting.order_by('start')[0]
    context_dict = {'uod_cadets': next_meeting.uod_cadets,
                    'uod_staff': next_meeting.uod_staff,
                    'uod_senior': next_meeting.uod_senior,
                    'start': next_meeting.start.time,
                    'end': next_meeting.end.time,
                    'activities': next_meeting.activities,
                    }
    return render(request, 'events/call_down.html', context_dict)


def schedule(request):
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    current_squadron = current_cadet.squadron
#    third_month = timezone.now().month + 2
    next_meeting = Event.objects.filter(squadron__iexact=current_squadron)
    next_meeting = next_meeting.filter(weekly_meeting__exact=False)
    next_meeting = next_meeting.filter(start__gte=timezone.now())
#    next_meeting = next_meeting.filter(start__month=third_month)
#    next_meeting = next_meeting.order_by('start')[0]
    months = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}
    context_dict = {'next_meeting': next_meeting,
                    'months': months}
    return render(request, 'events/schedule', context_dict)