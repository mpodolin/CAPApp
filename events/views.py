from django.shortcuts import render
from .models import Event
from promotions.models import Cadet
from django.utils import timezone
from dateutil import relativedelta

# Selects the next weekly meeting of the squadron for the call down
def call_down(request):
    # Find the squadron of the current cadet
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    current_squadron = current_cadet.squadron

    # Filter for the next weekly meeting of the current cadet
    next_meeting = Event.objects.filter(squadron__iexact=current_squadron)
    next_meeting = next_meeting.filter(weekly_meeting__exact=True)
    next_meeting = next_meeting.filter(start__gte=timezone.now())
    next_meeting = next_meeting.order_by('start')[0]

    # Render info
    context_dict = {'uod_cadets': next_meeting.uod_cadets,
                    'uod_staff': next_meeting.uod_staff,
                    'uod_senior': next_meeting.uod_senior,
                    'start': next_meeting.start.time,
                    'end': next_meeting.end.time,
                    'activities': next_meeting.activities,
                    }
    return render(request, 'events/call_down.html', context_dict)


def schedule(request):
    # Find the squadron of the current cadet
    current_cadet = Cadet.objects.get(username=request.user.get_username())
    current_squadron = current_cadet.squadron

    # Find the this and the next two months (and their years)
    first_date = timezone.now()
    second_date = first_date + relativedelta.relativedelta(months=1)
    third_date = second_date + relativedelta.relativedelta(months=1)
    first_month = first_date.month
    second_month = second_date.month
    third_month = third_date.month
    first_year = first_date.year
    second_year = second_date.year
    third_year = third_date.year

    # Filter all events to be just upcoming non-weekly meetings for the cadet
    next_meeting = Event.objects.filter(squadron__iexact=current_squadron)
    next_meeting = next_meeting.filter(weekly_meeting__exact=False)
    next_meeting = next_meeting.filter(start__gte=timezone.now())

    # Filter by month and then sort by start
    first_month_meeting = next_meeting.filter(start__month = first_month,
                                              start__year = first_year,)
    second_month_meeting = next_meeting.filter(start__month = second_month,
                                               start__year = second_year,)
    third_month_meeting = next_meeting.filter(start__month = third_month,
                                              start__year = third_year,)
    first_month_meeting = first_month_meeting.order_by('start')
    second_month_meeting = second_month_meeting.order_by('start')
    third_month_meeting = third_month_meeting.order_by('start')

    # Months and their names
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

    # Upcoming month names
    first_month_name = months[first_month]
    second_month_name = months[second_month]
    third_month_name = months[third_month]

    # Render info
    context_dict = {'first_month_meeting': first_month_meeting,
                    'second_month_meeting': second_month_meeting,
                    'third_month_meeting': third_month_meeting,
                    'first_month_name': first_month_name,
                    'second_month_name': second_month_name,
                    'third_month_name': third_month_name,}
    return render(request, 'events/schedule.html', context_dict)