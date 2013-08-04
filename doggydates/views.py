import dateutil.parser
import calendar
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from models import *
import json

WEEKDAYS = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
    }

def customers(request):
    if request.method == 'POST':
        d = json.loads(request.POST['data'])
        CustomerRow.objects.all().delete()
        for r in d[1:]:
            CustomerRow.objects.get_or_create(
               customer = r[0],
               day = r[1],
               group = r[2],
               walker = r[3],
               address = r[4],
               dog = r[5],
               cell = r[6],
               home = r[7],
               email = r[8],
               notes = r[9],
            )
            
        return HttpResponse('1')
    rows = CustomerRow.objects.all()
    return render(request, 'customers.html', {'rows': rows})


def changes(request):
    if request.method == 'POST':
        d = json.loads(request.POST['data'])
        ChangeRow.objects.all().delete()
        for r in d[1:]:
            if r[0].strip() and r[2].strip():
                ChangeRow.objects.get_or_create(
                    customer = r[0],
                    action = r[1],
                    date = dateutil.parser.parse(r[2]),
                    group = r[3])
        return HttpResponse('1')

    rows = ChangeRow.objects.all()
    return render(request, 'changes.html', {'rows': rows})

def schedule(request):
    if request.GET.get('date'):
        d = request.GET['date']
        date = dateutil.parser.parse(d)
        walkers = CustomerRow.objects.values_list('walker', flat=True).distinct()

        data = {}
        for w in walkers:
            cancels = ChangeRow.objects.filter(date = date, action="Cancel").values_list('customer', flat=True)
            data[w] = CustomerRow.objects.filter(walker=w, day=date.strftime('%A')).exclude(customer__in=cancels).order_by('group')
            
            adds = ChangeRow.objects.filter(date = date, action="Add")
            for a in adds:
                data[w] = list(data[w])
                c = CustomerRow.objects.filter(customer = a.customer)[0]
                if w == c.walker:
                    data[w] = list(data[w])
                    c.group = a.group
                    data[w].append(c)

            data[w].append(adds)
        
        return render(request, 'schedule.html', {'data': data})
        
    return render(request, 'schedule.html')     

def billing(request):
    customers = CustomerRow.objects.values_list('customer', flat=True).distinct()
    d = {}
    now = datetime.datetime.now()
    for c in customers:
        d[c] = {}
        d[c]['changes'] = ChangeRow.objects.filter(customer = c, date__month = now.month - 1)
        d[c]['regular'] = {}
        for recurring_event in CustomerRow.objects.filter(customer = c):
            if recurring_event.day.strip(): # deal with blanks
                d[c]['regular'][recurring_event.day] = len([1 for i in calendar.monthcalendar(now.year,
                                          now.month) if i[WEEKDAYS[recurring_event.day]] != 0])
    
    return render(request, 'billing.html', {'d': d})

