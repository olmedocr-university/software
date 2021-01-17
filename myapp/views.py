from django.shortcuts import render
from myapp.models import CollaborativeList, Song, Concert, Ticket
from decimal import Decimal
import math
from django.http import HttpResponse
import random


# Create your views here.
def addSongToPlaylist(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
        song = Song.objects.get(id=request.GET.get('song'))
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')
    except Song.DoesNotExist:
        return HttpResponse('"message" : "Song does not exist, invalid song id"')

    playlist.songs.add(song)
    playlist.save()
    response = '"Song ' + str(song.name) + " added to playlist " + str(playlist.name) + '"'
    return HttpResponse('"message" : ' + response)


def removeSongFromPlaylist(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
        song = Song.objects.get(id=request.GET.get('song'))
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')
    except Song.DoesNotExist:
        return HttpResponse('"message" : "Song does not exist, invalid song id"')

    playlist.songs.remove(song)
    playlist.save()
    response = '"Song ' + str(song.name) + " removed from playlist " + str(playlist.name) + '"'
    return HttpResponse('"message" : ' + response)


def sortList(request, playlistID):
    try:
        playlist = CollaborativeList.objects.get(id=playlistID)
    except CollaborativeList.DoesNotExist:
        return HttpResponse('"message" : "Playlist does not exist, invalid list id"')

    response = "[ "
    sortedList = playlist.songs.order_by('name')
    for song in sortedList:
        response += '"' + str(song) + '", '
    response += ' ]'
    return HttpResponse('"message" : ' + response)
  

# GET recognise_song
def recognise_song(request):
    try:
        random_song = Song.objects.get(id=random.randint(0, 6))
    except Song.DoesNotExist:
        return HttpResponse('"message" : "Could not recognise song"')

    response = '{\n"song_name" : "' + str(random_song.name) + \
               '",\n"song_artist" : "' + str(random_song.author) + \
               '",\n"song_album" : "' + str(random_song.album) + \
               '",\n"song_duration" : "' + str(random_song.duration) + '"\n},\n'

    return HttpResponse(response)

  
def getConcerts(request, lat, lon):
    nearBy_Concerts = list()

    try:
        concerts = Concert.objects.all()
        for item in concerts:
            distance = math.sqrt(math.pow(item.lat - Decimal(lat), 2) + math.pow(item.lon - Decimal(lon), 2))


            if distance < 500:
                nearBy_Concerts.append(item)
    except Concert.DoesNotExist:
        return HttpResponse('"message" : "concert does not exist"')

    response = "[ "
    for element in nearBy_Concerts:
        response += '"' + str(element) + '", '
    response += ' ]'
    return HttpResponse('"message" : ' + response)


def get_tickets(request, concert_id):
    try:
        concert = Concert.objects.get(id=concert_id)
        tickets = concert.ticket_set.all()
    except Ticket.DoesNotExist:
        return HttpResponse('"message" : "Tickets do not exist for this concert"')
    except Concert.DoesNotExist:
        return HttpResponse('"message" : "Concert does not exist, invalid concert id"')

    response = '[ '
    for ticket in tickets:
        response += '{' + \
            '"zone": "' + str(ticket.zone) + '",'\
            '"price": ' + str(ticket.price) + \
            '},'
    response = response[:-1]
    response += ' ]'
    return HttpResponse('"message" : ' + response)
