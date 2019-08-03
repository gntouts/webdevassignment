from patrasktel.models import Route, Stop, Schedule, Announcement, Ticket, Contact, About
from django.shortcuts import render
from django.views import generic
# Create your views here.


def index(request):
    contact = Contact.objects.all().first()
    announcement = Announcement.objects.all().first()
    context = {
        'contact': contact,
        'announcement': announcement,
    }
    return render(request, 'index.html', context=context)


def announcement(request):
    announcement_list = Announcement.objects.all()
    contact = Contact.objects.all().first()
    context = {
        'announcement_list': announcement_list,
        'contact': contact,
    }
    return render(request, 'announcement_list.html', context=context)


def route(request):
    stops = Stop.objects.all()
    stop_list = []
    route_list = Route.objects.all()

    contact = Contact.objects.all().first()
    context = {
        'route_list': route_list,
        'stop_list': stop_list,
        'contact': contact,
    }
    return render(request, 'route_list.html', context=context)


def tickets(request):
    ATickets = Ticket.objects.filter(zone='A')
    an = ATickets.filter(price_cat='n').first()
    ar = ATickets.filter(price_cat='r').first()
    BTickets = Ticket.objects.filter(zone='B')
    bn = BTickets.filter(price_cat='n').first()
    br = BTickets.filter(price_cat='r').first()
    contact = Contact.objects.all().first()
    context = {
        'an': an,
        'ar': ar,
        'bn': bn,
        'br': br,
        'contact': contact,
    }
    return render(request, 'tickets.html', context=context)


def contact(request):
    contact = Contact.objects.all().first()
    context = {
        'contact': contact,
    }
    return render(request, 'contact.html', context=context)


def about(request):
    about = About.objects.all().first()
    contact = Contact.objects.all().first()
    context = {
        'about': about,
        'contact': contact,
    }
    return render(request, 'about.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
