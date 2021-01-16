from django.shortcuts import render
from myapp.models import CollaborativeList, Song, Concert
from decimal import Decimal
import math
from django.http import HttpResponse


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
