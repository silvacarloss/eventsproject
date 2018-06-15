from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import UserTag, EventTag, Tag, User, Event

def index(request):
    latest_event_list = Event.objects.order_by('-date')
    template = loader.get_template('rolefinder/index.html')
    context = {
        'events' : latest_event_list,
    }
    return render(request, 'rolefinder/index.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    
    return render(request, 'rolefinder/event_detail.html', {'event': event})

def new_event(request):
    tags_list = Tag.objects.all()
    context = {
        'tags_list' : tags_list,
    }    
    return render(request, 'rolefinder/new_event.html', context)

def save(request):
    title = request.POST['title']
    description = request.POST['description']
    address = request.POST['address']
    datetime = request.POST['date']
    datetime += " " + request.POST['time']
    picture = request.POST['picture']
    price = request.POST['price']
    tagsselected = request.POST['tagsselected']

    tags_list = tagsselected.split(",")

    EventInstance = Event.objects.create(
        title = title,
        description = description,
        address = address,
        date = datetime,
        picture = "picture",
        price = price
    )
    for x in range(1, tags_list.__len__()):
        tag = get_object_or_404(Tag, pk = tags_list[x])
        event_tag_instance = EventTag.objects.create(
            tag = tag,
            event = EventInstance 
        )

    return index(request)

def delete(request, event_id):
    Event.objects.filter(id=event_id).delete()
    return index(request)

